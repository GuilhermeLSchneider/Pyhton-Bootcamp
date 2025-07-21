import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import datetime

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

def choose_branch():
    # Exemplo: branch baseado no horário atual
    hour = datetime.now().hour
    if hour < 12:
        return 'morning_task'
    elif hour < 18:
        return 'afternoon_task'
    else:
        return 'evening_task'

with DAG(
    dag_id='branch_pratica_dag',
    default_args=default_args,
    schedule_interval="@once"
) as dag:

    start = DummyOperator(task_id='start')

    branch = BranchPythonOperator(
        task_id='branching',
        python_callable=choose_branch
    )

    morning = DummyOperator(task_id='morning_task')
    afternoon = DummyOperator(task_id='afternoon_task')
    evening = DummyOperator(task_id='evening_task')

    end = DummyOperator(task_id='end')

    start >> branch
    branch >> [morning, afternoon, evening]
    [morning, afternoon, evening] >> end
