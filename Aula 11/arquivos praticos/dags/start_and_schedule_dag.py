from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    # O ultimo argumento no 'start_date' é a hora que a DAG será executada
    # O horário é no padrão UTC
    'start_date': datetime(2024, 12, 30, 1),
    'owner': 'Airflow'
}

# O schedule_interval é uma string que aceita, nesse caso, uma cron expression: * * * * * (minutos horas dias-do-mês meses dias-da-semana)
# um valor indicando 0 0 * * * significa que a DAG será executada todos os dias à meia-noite
# um valor indicando 0 0 1 * * significa que a DAG será executada todos os dias do mês à meia-noite no primeiro dia do mês
# crontab.guru é um site que ajuda a criar cron expressions

with DAG(dag_id='start_and_schedule_dag', schedule_interval=timedelta(hours=1), default_args=default_args) as dag:
    
    # Task 1
    dummy_task_1 = DummyOperator(task_id='dummy_task_1')
    
    # Task 2
    dummy_task_2 = DummyOperator(task_id='dummy_task_2')
    
    dummy_task_1 >> dummy_task_2
    
    # Logs to help you (printed from the web server logs)
    # Uncomment when you use the DAG, comment when not
    # run_dates = dag.get_run_dates(start_date=dag.start_date)
    # next_execution_date = run_dates[-1] if len(run_dates) != 0 else None
    # print('[DAG:start_and_schedule_dag] start_date: {0} - schedule_interval: {1} - Last execution_date: {2} - next execution_date {3} in UTC'.format(
    #     dag.default_args['start_date'], 
    #     dag._schedule_interval, 
    #     dag.latest_execution_date, 
    #     next_execution_date
    #     ))