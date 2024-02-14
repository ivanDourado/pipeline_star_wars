# Importa a classe DAG do módulo airflow.
from airflow import DAG
# Importa o PythonOperator do módulo de operadores do python.
from airflow.operators.python_operator import PythonOperator
# Importa a classe datetime do módulo datetime para definir datas e horas.
from datetime import datetime, timedelta
# biblioteca recomendada para timezone
import pendulum

# Adiciona o diretório utils ao path para permitir importações dos scripts.
import sys
sys.path.append('/opt/airflow/dags/utils')

# Importa as funções dos scripts localizados no diretório utils.
from script_request import main as extract_and_save_json
from script_results import generate_results_json as generate_results_json

# Define argumentos padrão que serão passados para cada tarefa do DAG.
default_args = {
    'owner': 'airflow',  # Identifica o usuário ou entidade que possui a DAG, para fins de gestão e responsabilidade
    'depends_on_past': False,  # Indica se uma instância de tarefa deve depender do sucesso da tarefa na execução anterior
    'email_on_failure': False,  # Desativa o envio de emails em caso de falha da tarefa
    'email_on_retry': False,  # Desativa o envio de emails em caso de nova tentativa após falha
    'retries': 5,  # Define o número máximo de tentativas em caso de falha da tarefa
    'retry_delay': timedelta(minutes=5),  # Define o intervalo de tempo entre as tentativas em caso de falha
    # Define a data e hora de início da primeira execução da DAG, utilizando pendulum para especificar o fuso horário
    'start_date': pendulum.datetime(2024, 2, 1, tz='America/Sao_Paulo'),
    'schedule_interval': '0 0 * * 0',  # Define a periodicidade da execução da DAG como semanal, à meia-noite de cada domingo
    'catchup':False,  # Impede a execução de DAGs para períodos anteriores à data atual
}

# Cria uma instância DAG, que é um conjunto de tarefas organizadas com dependências e cronograma.
with DAG('star_wars_data_pipeline', default_args=default_args) as dag:
    # Cria uma tarefa usando PythonOperator para extrair dados e salvá-los.
    extract = PythonOperator(
        task_id='extract_and_save_all_data',
        python_callable=main,
    )
    # Cria outra tarefa para processar os dados e criar o arquivo results no formato pedido
    results  = PythonOperator(
        task_id='create_results_json',
        python_callable=generate_results_json,
    ) 
    # Define a ordem de execução das tarefas usando o operador de bitshift.
    # As tarefas de extração de dados serão executadas antes da tarefa de processamento.
    extract >> results   