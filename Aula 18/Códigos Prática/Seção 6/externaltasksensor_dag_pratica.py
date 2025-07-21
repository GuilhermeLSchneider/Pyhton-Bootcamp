import airflow.utils.dates
from airflow import DAG
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    "owner": "airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

with DAG(dag_id="externalsens_pratica_dag", default_args=default_args, schedule_interval="@daily") as dag:
    wait_for_data = ExternalTaskSensor(
        task_id="wait_for_data",
        external_dag_id="data_pipeline_dag",
        external_task_id="process_data",
        mode="poke", # modo poke significa que o sensor irá verificar periodicamente (é o default mode)
        timeout=600
    )

    notify = DummyOperator(task_id="notify")

    wait_for_data >> notify