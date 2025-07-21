from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2025, 1, 1),
    'owner': 'Airflow',
}

with DAG(dag_id='processamento_de_dados_dag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    
    extrair_dados = BashOperator(task_id='extrair_dados', bash_command='echo "Extraindo dados da fonte"')

    transformar_dados = BashOperator(task_id='transformar_dados', bash_command='echo "Transformando dados"')

    carregar_dados = BashOperator(task_id='carregar_dados', bash_command='echo "Carregando dados no destino"')

    validar_dados = BashOperator(task_id='validar_dados', bash_command='echo "Validando dados carregados"')

    gerar_relatorio = BashOperator(task_id='gerar_relatorio', bash_command='echo "Gerando relatório"')

    notificar = BashOperator(task_id='notificar', bash_command='echo "Enviando notificação"')

    tarefa_final = DummyOperator(task_id='tarefa_final')

    [extrair_dados, transformar_dados, carregar_dados, validar_dados, gerar_relatorio, notificar] >> tarefa_final