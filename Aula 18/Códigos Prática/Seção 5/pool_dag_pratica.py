from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 1, 1),
    'owner': 'Airflow',
}

with DAG(
    dag_id='pool_pratica_dag',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False
) as dag:

    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Task 1 em execução"',
        pool='pool'
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Task 2 em execução"',
        pool='pool'
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Task 3 em execução"',
        pool='pool'
    )

    [task_1, task_2, task_3]
