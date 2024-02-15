# Star Wars Data Pipeline Project

<h6>Não fala inglês? <a href="https://github.com/ivanDourado/star_wars/blob/main/README.md">Clique Aqui</a> para visualizar essa página em português.</h6>

This project involves the creation of an ETL (Extract, Transform, Load) process to gather data from the Star Wars API (SWAPI), transform the data as required, and load it into structured JSON files and CSV reports. The process is orchestrated using Apache Airflow, ensuring a scalable and manageable workflow.

## Overview

![image](https://github.com/ivanDourado/star_wars/assets/85656465/132efe60-2854-4bb5-a058-2ff4011c619f)


The project is structured around three main components:

- Script for Data Extraction (`script_request.py`): Makes API requests to SWAPI to fetch data related to people, films, and vehicles. The data is then saved into JSON files organized by category and year.
  
- Script for Data Transformation (`script_result.py`): Transforms the data into the desired format, focusing on people and films data, and generates a summary CSV report showing the count of records fetched for each category.

- Airflow DAG (`star_wars_data_pipeline.py`): Orchestrates the ETL process, utilizing PythonOperator to execute the functions defined in the previous scripts.

### .gitignore Configuration

To ensure the repository remains clean and only includes source code, the following patterns are added to .gitignore:

*.log
logs/*
films/*
people/*
vehicles/*
results/*
*.json
*.pyc
__pycache__/
plugins/

This setup prevents data files and logs from being committed to the repository, aligning with best practices for data lake management and code repository hygiene.

### Script for Data Extraction (script_request.py)

The script performs the following actions:

- API Data Fetching: Utilizes requests library to paginate through the SWAPI endpoints, collecting data for people, films, and vehicles.
  
- JSON File Saving: Organizes and saves the fetched data into JSON files within directories structured by category and year, e.g., People/{year}/*.json.

### Script for Data Transformation (script_result.py)

This script transforms the fetched JSON data into the specified format and generates a results2.json file under the /opt/airflow/results directory, summarizing the data for further analysis.

### Airflow DAG (star_wars_data_pipeline.py)

The DAG is set up with two tasks using PythonOperator:

- Data Extraction Task: Calls a function to execute the data fetching and saving logic from script_request.py.

- Data Transformation Task: Invokes a function to transform the data and generate the summary report as per script_result.py.

## Execution

The ETL process is initiated through the Airflow web interface after starting the Airflow services using Docker Compose in the terminal. The workflow's progress and outputs can be monitored via the Airflow UI and the logs generated for each task.

## Commit Standards

Commits follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) standard, aiming for clear and descriptive commit messages that outline the changes made.

## Documentation and Comments

Despite the redundancy in some comments, they are included throughout the code for educational purposes, reflecting the transition from analysis to data engineering and aiding in knowledge assimilation.

## Conclusion

This project exemplifies a basic yet powerful use of Airflow to automate the data pipeline process, from extracting data from an external API to transforming and loading it into a structured format for analysis. It demonstrates the versatility and capability of Airflow in managing data workflows, ensuring data reliability and efficiency in processing.
