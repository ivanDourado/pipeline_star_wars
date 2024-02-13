# Importa a classe DAG do módulo airflow.
from airflow import DAG
# Importa o PythonOperator do módulo de operadores do python.
from airflow.operators.python_operator import PythonOperator
# Importa a classe datetime do módulo datetime para definir datas e horas.
from datetime import datetime, timedelta