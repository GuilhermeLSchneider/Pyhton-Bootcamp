import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "start_date": airflow.utils.dates.days_ago(1),
    "owner": "Airflow"
}

def print_square(**context):
    number = context["dag_run"].conf.get("number", 0)
    square = number ** 2
    print(f"O quadrado de {number} é {square}")

with DAG(dag_id="triggerdagop_target_pratica", default_args=default_args, schedule_interval=None) as dag:

    t1 = PythonOperator(
        task_id="print_square",
        python_callable=print_square,
    )

    t2 = BashOperator(
        task_id="bash_echo",
        bash_command='echo "Número recebido: {{ dag_run.conf["number"] if dag_run else "" }}"'
    )

    t1 >> t2