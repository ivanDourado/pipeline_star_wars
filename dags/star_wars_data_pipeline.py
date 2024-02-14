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
from script_request import main as main
from script_results import generate_results_json as generate_results_json

# Define argumentos padrão que serão passados para cada tarefa do DAG.
default_args = {
    'owner': 'airflow',  # Define o proprietário do DAG, geralmente 'airflow' ou o nome de usuário do criador do DAG.
    'start_date': datetime.now() + timedelta(seconds=10) , # Define a data de início da execução do DAG.
    'schedule_interval': None,
    'retries': 5,  # Define o número de tentativas de reexecução em caso de falha.
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