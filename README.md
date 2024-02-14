# Projeto de Pipeline de Dados Star Wars

<h6>Do not speak Portuguese? <a href="https://github.com/ivanDourado/star_wars/blob/main/README-en.md">Click Here</a> to view this page in English.</h6>

Este projeto envolve a criação de um processo ETL (Extract, Transform, Load) para coletar dados da API Star Wars (SWAPI), transformar os dados conforme necessário e carregar em arquivos JSON estruturados e relatórios CSV. O processo é orquestrado usando o Apache Airflow, garantindo um fluxo de trabalho escalável e gerenciável.

## Visão Geral

O projeto é estruturado em torno de três componentes principais:

- **Script de Extração de Dados (`script_request.py`)**: Faz requisições à API SWAPI para buscar dados relacionados a pessoas, filmes e veículos. Os dados são então salvos em arquivos JSON organizados por categoria e ano.
  
- **Script de Transformação de Dados (`script_result.py`)**: Transforma os dados no formato desejado, focando nos dados de pessoas e filmes, e gera um relatório resumo em CSV mostrando a contagem de registros buscados para cada categoria.

- **DAG do Airflow (`star_wars_data_pipeline.py`)**: Orquestra o processo ETL, utilizando PythonOperator para executar as funções definidas nos scripts anteriores.

### Configuração do .gitignore

Para garantir que o repositório permaneça limpo e inclua apenas o código-fonte, os seguintes padrões são adicionados ao `.gitignore`:




.log

logs/

films/*

people/*

vehicles/*

results/*

*.json

*.pyc

pycache/

plugins/


Essa configuração impede que arquivos de dados e logs sejam commitados no repositório, alinhando-se às melhores práticas para gestão de data lake e higiene do repositório de código.

### Script para Extração de Dados (`script_request.py`)

O script realiza as seguintes ações:

- **Busca de Dados da API**: Utiliza a biblioteca `requests` para paginar através dos endpoints da SWAPI, coletando dados para pessoas, filmes e veículos.
  
- **Salvamento de Arquivos JSON**: Organiza e salva os dados buscados em arquivos JSON dentro de diretórios estruturados por categoria e ano, por exemplo, `People/{year}/*.json`.

### Script para Transformação de Dados (`script_result.py`)

Este script transforma os dados JSON buscados no formato especificado e gera um arquivo `results2.json` no diretório `/opt/airflow/results`, resumindo os dados para análises futuras.

### DAG do Airflow (`star_wars_data_pipeline.py`)

A DAG é configurada com duas tarefas usando PythonOperator:

- **Tarefa de Extração de Dados**: Chama uma função para executar a lógica de busca e salvamento de dados de `script_request.py`.

- **Tarefa de Transformação de Dados**: Invoca uma função para transformar os dados e gerar o relatório resumo conforme `script_result.py`.

## Execução

O processo ETL é iniciado através da interface web do Airflow após iniciar os serviços do Airflow usando Docker Compose no terminal. O progresso do fluxo de trabalho e as saídas podem ser monitorados via UI do Airflow e os logs gerados para cada tarefa.

## Padrões de Commit

Os commits seguem o padrão [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/), visando mensagens de commit claras e descritivas que delineiam as mudanças feitas.

## Documentação e Comentários

Apesar da redundância em alguns comentários, eles são incluídos em todo o código para fins educacionais, refletindo a minha transição de análise para engenharia de dados e auxiliando na assimilação do conhecimento.

## Conclusão

Este projeto exemplifica um uso básico, porém poderoso, do Airflow para automatizar o processo de pipeline de dados, desde a extração de dados de uma API externa até a transformação e carga em um formato estruturado para análise. Ele demonstra a versatilidade e capacidade do Airflow na gestão de fluxos de trabalho de dados, garantindo confiabilidade dos dados e eficiência no processamento.
