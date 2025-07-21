from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 1, 1),
    'owner': 'Airflow',
}

def parallel_task(task_number):
    print(f"Tasks paralelas em execução {task_number}")

def final_task():
    print("Todas as tasks foram finalizadas!")

with DAG(dag_id='parallel_pratica_dag', schedule_interval=None, default_args=default_args, catchup=False) as dag:

    parallel_tasks = [
        PythonOperator(
            task_id=f'parallel_task_{i}',
            python_callable=parallel_task,
            op_args=[i]
        ) for i in range(1, 4)
    ]

    join_task = PythonOperator(
        task_id='join_task',
        python_callable=final_task
    )

    parallel_tasks >> join_task