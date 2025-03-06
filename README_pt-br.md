# Projeto de Pipeline de Dados Star Wars

<h6>Do not speak Portuguese? <a href="https://github.com/ivanDourado/case-fake-store/blob/master/README.md">Click Here</a> to view this page in English.</h6>

Este projeto envolve a criação de um processo ETL (Extract, Transform, Load) para coletar dados da API Star Wars (SWAPI), transformar os dados conforme necessário e carregar em arquivos JSON estruturados e relatórios CSV. O processo é orquestrado usando o Apache Airflow, garantindo um fluxo de trabalho escalável e gerenciável.

## Visão Geral

![image](https://github.com/ivanDourado/star_wars/assets/85656465/c6cd9104-8db2-450e-bd01-44e33e7844f2)


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

## Instruções de Execução

1. Abra um terminal e navegue até o diretório onde o arquivo `docker-compose.yaml` está localizado.
2. Inicie os serviços do Airflow executando o comando `docker compose up -d`.
3. Após os serviços estarem rodando, abra um navegador e acesse `http://localhost:8080` para abrir a interface web do Airflow.
4. Faça login na interface do Airflow usando as credenciais padrão (usuário e senha `airflow`).
5. Navegue até a seção "DAGs" na interface do Airflow.
6. Localize a DAG `star_wars_data_pipeline` e clique para acessar seus detalhes.
7. Ative a DAG clicando no botão de alternância ao lado do nome da DAG, se necessário.
8. Inicie uma execução da DAG clicando no botão "Trigger DAG" e confirme a ação.
9. Acompanhe o progresso da execução da DAG e visualize os logs para cada tarefa executada através da interface do Airflow.

Siga essas instruções para executar o processo ETL e monitorar o progresso e as saídas do fluxo de trabalho do case Star Wars.

## Padrões de Commit

Os commits seguem o padrão [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/), visando mensagens de commit claras e descritivas que delineiam as mudanças feitas.

## Documentação e Comentários

Apesar da redundância em alguns comentários, eles são incluídos em todo o código para fins educacionais, refletindo a minha transição de análise para engenharia de dados e auxiliando na assimilação do conhecimento.

## Conclusão

Este projeto exemplifica um uso básico, porém poderoso, do Airflow para automatizar o processo de pipeline de dados, desde a extração de dados de uma API externa até a transformação e carga em um formato estruturado para análise. Ele demonstra a versatilidade e capacidade do Airflow na gestão de fluxos de trabalho de dados, garantindo confiabilidade dos dados e eficiência no processamento.
