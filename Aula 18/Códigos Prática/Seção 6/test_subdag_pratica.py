import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator

def create_subdag(parent_dag_name, child_dag_name, args):
    subdag = DAG(
        dag_id=f"{parent_dag_name}.{child_dag_name}",
        default_args=args,
        schedule_interval="@once",
    )

    t1 = DummyOperator(
        task_id='task_1',
        dag=subdag
    )

    t2 = DummyOperator(
        task_id='task_2',
        dag=subdag
    )

    t1 >> t2
    return subdag

DAG_NAME = "subdag_pratica"

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1)
}

with DAG(dag_id=DAG_NAME, default_args=default_args, schedule_interval="@once") as dag:
    start = DummyOperator(task_id='start')

    subdag_a = SubDagOperator(
        task_id='subdag_a',
        subdag=create_subdag(DAG_NAME, 'subdag_a', default_args)
    )

    subdag_b = SubDagOperator(
        task_id='subdag_b',
        subdag=create_subdag(DAG_NAME, 'subdag_b', default_args)
    )

    end = DummyOperator(task_id='end')

    start >> subdag_a >> subdag_b >> end