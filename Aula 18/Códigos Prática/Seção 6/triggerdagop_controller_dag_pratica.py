import airflow.utils.dates
from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.empty import EmptyOperator

default_args = {
    "owner": "airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

with DAG(dag_id="triggerdagop_controller_pratica", default_args=default_args, schedule_interval="@once") as dag:

    trigger = TriggerDagRunOperator(
        task_id="trigger_target_pratica",
        trigger_dag_id="triggerdagop_target_pratica",
        conf={"number": 7},
    )

    end = EmptyOperator(task_id="end")

    trigger >> end