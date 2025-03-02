import airflow
from airflow import DAG
from airflow.sensors.file_sensor import FileSensor
from airflow.sensors.http_sensor import HttpSensor
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
# from airflow.operators.hive_operator import HiveOperator
# from airflow.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.slack_operator import SlackAPIPostOperator
from datetime import datetime, timedelta

# Importando bibliotecas necessárias
import csv
import requests
import json

# Argumentos default
default_args = {
    	'owner': 'airflow',
    	'start_date': datetime(2025, 1, 1),
    	'depends_on_past': False,
    	'email_on_failure': False,
   	    'email_on_retry': False,
    	'email': 'guilhermeloan@alunos.utfpr.edu.br',
    	'retries': 1,
    	'retries_delay': timedelta(minutes=5),
}

def download_rates():
    with open('/usr/local/airflow/dags/files/forex_currencies.csv') as forex_currencies:
        reader = csv.DictReader(forex_currencies, delimiter=';')
        for row in reader:
            base = row['base']
            with_pairs = row['with_pairs'].split(' ')
            # Precisei alterar o link do site por conta de necessitar uma access_key vinculado por usuario
            indata = requests.get('https://api.exchangeratesapi.io/v1/latest?access_key=d326b904e3f656f8d7122544a6101ffc&base=' + base).json()
            outdata = {'base': base, 'rates': {}, 'last_update': indata['date']}
            for pair in with_pairs:
                outdata['rates'][pair] = indata['rates'][pair]
            with open('/usr/local/airflow/dags/files/forex_rates.json', 'a') as outfile:
                json.dump(outdata, outfile)
                outfile.write('\n')

with DAG(dag_id="forex_data_pipeline_final", 
        schedule_interval="@daily", 
        default_args=default_args, 
        catchup=False) as dag:

    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        method="GET",
        http_conn_id="forex_api",
        endpoint="latest",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )

    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20
    )

    downloading_rates = PythonOperator(
        task_id="downloading_rates",
        python_callable=download_rates
    )

    saving_rates = BashOperator(
        task_id="saving_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex && \
            hdfs dfs -put -f $AIRFLOW_HOME/dags/files/forex_rates.json /forex
            """
    )

    # creating_forex_rates_table = HiveOperator(
    #     task_id="creating_forex_rates_table",
    #     hive_cli_conn_id="hive_conn",
    #     hql="""
    #         CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
    #             base STRING,
    #             last_update DATE,
    #             eur DOUBLE,
    #             usd DOUBLE,
    #             nzd DOUBLE,
    #             gbp DOUBLE,
    #             jpy DOUBLE,
    #             cad DOUBLE
    #             )
    #         ROW FORMAT DELIMITED
    #         FIELDS TERMINATED BY ','
    #         STORED AS TEXTFILE
    #     """
    # )

    # forex_processing = SparkSubmitOperator(
    #     task_id="forex_processing",
    #     conn_id="spark_conn",
    #     application="/usr/local/airflow/dags/scripts/forex_processing.py",
    #     verbose=False
    # )

    sending_email_notification = EmailOperator(
        task_id="sending_email",
        to="guilhermeloan@alunos.utfpr.edu.br",
        subject="forex_data_pipeline",
        html_content="""
            <h3>forex_data_pipeline succeeded</h3>
            """
        )

    sending_slack_notification = SlackAPIPostOperator(
        task_id="sending_slack",
        token="xoxp-753801195270-740121926339-751642514144-8391b800988bed43247926b03742459e",
        username="airflow",
        text="DAG forex_data_pipeline: DONE",
        channel="#airflow-exploit"
    )

    # Definindo a ordem de execução das tasks a partir do operador de fluxo '>>'
    # is_forex_rates_available deve ser executado antes de is_forex_currencies_file_available e assim por diante
    
    # is_forex_rates_available >> is_forex_currencies_file_available >> downloading_rates >> saving_rates
    # saving_rates >> creating_forex_rates_table >> forex_processing 
    # forex_processing >> sending_email_notification >> sending_slack_notification
    
    is_forex_rates_available >> is_forex_currencies_file_available >> downloading_rates >> saving_rates
    saving_rates >> sending_email_notification >> sending_slack_notification