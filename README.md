# Projeto de Pipeline de Dados Star Wars

<h6>Do not speak Portuguese? <a href="https://github.com/ivanDourado/star_wars/blob/main/README-en.md">Click Here</a> to view this page in English.</h6>

Este projeto envolve a criação de um processo ETL (Extract, Transform, Load) para coletar dados da API Star Wars (SWAPI), transformar os dados conforme necessário e carregar em arquivos JSON estruturados e relatórios CSV. O processo é orquestrado usando o Apache Airflow, garantindo um fluxo de trabalho escalável e gerenciável.

## Visão Geral
{"type":"excalidraw/clipboard","elements":[{"type":"line","version":2486,"versionNonce":200104433,"isDeleted":false,"id":"miKonR8RArMt6gmqYjEwW","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":962.4831014065412,"y":103.51876366307228,"strokeColor":"#000000","backgroundColor":"#000000","width":15.52805208181219,"height":14.605645223129823,"seed":1902423007,"groupIds":["sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[0.23190665565902752,6.98702689236363],[1.9909671080694653,13.067306217906113],[8.480625063698136,14.605645223129823],[15.52805208181219,14.108276286394865],[10.667122946465673,8.996248593924948],[4.8863114352428605,3.730064983571429],[0,0]]},{"type":"line","version":549,"versionNonce":1978594257,"isDeleted":false,"id":"PhztAISNzkkqglwyUUKSp","fillStyle":"cross-hatch","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":962.4608595814764,"y":103.54973741953089,"strokeColor":"#000000","backgroundColor":"transparent","width":45.04283451795358,"height":0,"seed":1354881023,"groupIds":["5pRGPORLYhHawHhNYv_By","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[-45.04283451795358,0]]},{"type":"line","version":605,"versionNonce":1147294129,"isDeleted":false,"id":"dmE30Bqn0ddQgF6BMM33K","fillStyle":"cross-hatch","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":917.5230848460858,"y":103.55014374211993,"strokeColor":"#000000","backgroundColor":"transparent","width":0,"height":86.98687282122496,"seed":2145681439,"groupIds":["5pRGPORLYhHawHhNYv_By","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[0,86.98687282122496]]},{"type":"line","version":560,"versionNonce":208597905,"isDeleted":false,"id":"6RWfvMwBK24HQ-dqsl6Yd","fillStyle":"cross-hatch","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":917.4420581882683,"y":190.5211491282293,"strokeColor":"#000000","backgroundColor":"transparent","width":60.86766746456416,"height":0,"seed":1623008319,"groupIds":["5pRGPORLYhHawHhNYv_By","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[60.86766746456416,0]]},{"type":"line","version":563,"versionNonce":1380735345,"isDeleted":false,"id":"qLEtZjvuKqXO-3z8jR7OR","fillStyle":"cross-hatch","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":978.2323912182642,"y":190.82840306619124,"strokeColor":"#000000","backgroundColor":"transparent","width":0.04915659589316011,"height":73.341599414468,"seed":1126974559,"groupIds":["5pRGPORLYhHawHhNYv_By","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[0.04915659589316011,-73.341599414468]]},{"type":"line","version":518,"versionNonce":658637649,"isDeleted":false,"id":"mB8FLCPnBEYxLy2Xm1qra","fillStyle":"cross-hatch","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":962.0796105446079,"y":103.4208601078864,"strokeColor":"#000000","backgroundColor":"transparent","width":16.105976238399123,"height":14.61678699389931,"seed":654467199,"groupIds":["5pRGPORLYhHawHhNYv_By","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[16.105976238399123,14.61678699389931]]},{"type":"line","version":1685,"versionNonce":128414001,"isDeleted":false,"id":"1qReyIWd_HayBk9X8xEOa","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":919.2927600934742,"y":154.29762509780466,"strokeColor":"#000000","backgroundColor":"#fff","width":76.04339967409842,"height":23.690133361177104,"seed":1040185503,"groupIds":["sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[28.235523929623003,0],[60.32134657692195,0.21342462487547498],[65.45507820048977,1.6006846865660045],[67.48718030148542,6.722875683577271],[67.59413304364303,16.006846865660204],[65.98984191127799,21.87602404973561],[60.321346576921925,23.476708736301596],[28.556382156096046,23.690133361177104],[-0.4278109686306638,23.47670873630165],[-6.096306302986783,21.6625994248601],[-8.449266630455394,16.43369611541112],[-8.235361146140068,6.829587996014987],[-5.668495334356166,1.4939723741282818],[0,0]]},{"type":"text","version":523,"versionNonce":2028217105,"isDeleted":false,"id":"WezLpcAwMRsM1BeOSsCAh","fillStyle":"cross-hatch","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":925.917908221505,"y":152.1721430669747,"strokeColor":"#000000","backgroundColor":"transparent","width":46.19640235173015,"height":26.534297218555754,"seed":768969919,"groupIds":["sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"fontSize":16.91929484088319,"fontFamily":1,"text":"JSON","textAlign":"left","verticalAlign":"top","containerId":null,"originalText":"JSON","lineHeight":1.5682862358092613,"baseline":17},{"type":"line","version":375,"versionNonce":1735366897,"isDeleted":false,"id":"c8wVcrUnq_ySqI-YjHEyR","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":923.8673833590275,"y":118.83455753807908,"strokeColor":"#000000","backgroundColor":"#ffffff","width":33.22548136037997,"height":0,"seed":304323807,"groupIds":["d5NlDoePZVGqAEC5AQk_c","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[33.22548136037997,0]]},{"type":"line","version":620,"versionNonce":1154568913,"isDeleted":false,"id":"bWB_u44kRsRvwtVcQcEcd","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":923.9093290113665,"y":124.9630406439529,"strokeColor":"#000000","backgroundColor":"#ffffff","width":43.08349869835954,"height":0,"seed":1048226047,"groupIds":["d5NlDoePZVGqAEC5AQk_c","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[43.08349869835954,0]]},{"type":"line","version":634,"versionNonce":1705038001,"isDeleted":false,"id":"bdq6G1YD2ZnIPEk206Y4s","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":923.9244526886388,"y":131.21351594843188,"strokeColor":"#000000","backgroundColor":"#ffffff","width":43.08349869835954,"height":0,"seed":1079718175,"groupIds":["d5NlDoePZVGqAEC5AQk_c","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[43.08349869835954,0]]},{"type":"line","version":679,"versionNonce":528847505,"isDeleted":false,"id":"KwLYf_EY3qD3XrA96Eyzb","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":923.9278420355712,"y":137.4695328175348,"strokeColor":"#000000","backgroundColor":"#ffffff","width":43.08349869835954,"height":0,"seed":557167935,"groupIds":["d5NlDoePZVGqAEC5AQk_c","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[43.08349869835954,0]]},{"type":"line","version":696,"versionNonce":657922161,"isDeleted":false,"id":"B7EUGJAzS9zGr169HRDW8","fillStyle":"solid","strokeWidth":1,"strokeStyle":"solid","roughness":1,"opacity":100,"angle":0,"x":923.8758313648966,"y":144.4587655501483,"strokeColor":"#000000","backgroundColor":"#ffffff","width":43.08349869835954,"height":0,"seed":1751823711,"groupIds":["d5NlDoePZVGqAEC5AQk_c","sWkIc4KV7w34I1TwtJmcF"],"frameId":null,"roundness":{"type":2},"boundElements":[],"updated":1707956351365,"link":null,"locked":false,"startBinding":null,"endBinding":null,"lastCommittedPoint":null,"startArrowhead":null,"endArrowhead":null,"points":[[0,0],[43.08349869835954,0]]}],"files":{}}
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
