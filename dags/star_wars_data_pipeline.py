# Importa a classe DAG do módulo airflow.
from airflow import DAG
# Importa o PythonOperator do módulo de operadores do python.
from airflow.operators.python_operator import PythonOperator
# Importa a classe datetime do módulo datetime para definir datas e horas.
from datetime import datetime, timedelta

# Adiciona o diretório utils ao path para permitir importações dos scripts.
import sys
sys.path.append('/opt/airflow/dags/utils')
