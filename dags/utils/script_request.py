import requests # Importa a biblioteca para fazer requisições HTTP
import json # Importa a biblioteca para manipular dados no formato JSON
from pathlib import Path # Importa a classe Path para manipular caminhos de arquivos/diretórios
import csv  # Usada para escrever em arquivos CSV.
from datetime import datetime  # Usada para trabalhar com datas e horas.


def fetch_all_data_from_endpoint(endpoint):
    """Coleta todos os dados paginados de um endpoint da SWAPI."""#docstring
    base_url = 'https://swapi.dev/api/' # Define a URL da API
    results = [] # Lista para armazenar todos os dados coletados
    url = f'{base_url}{endpoint}/' # Monta a URL do endpoint específico
    while url: # Enquanto houver uma URL para processar
        response = requests.get(url) # faz a requisiçõ à API
        if response.status_code == 200: # Se a requisição foi bem-sucedida
            data = response.json() # Converte a resposta em JSON
            results.extend(data['results']) # Adiciona os resultados à lista de dados
            url = data['next'] # Atualiza a URL para a próxima página de dados
        else: # Se a requisição falhou
            print("Falha na requisição: Status", response.status_code)
            break # encerra o Loop
    print('Dados coletados da API')
    return results # Retorna a lista de dados coletados

def save_json(data, year, category): 
    # Docstring
    """Salva os dados em um arquivo JSON dentro de um diretório específico do ano."""
    directory = Path(f"{category}/{year}") # Define o caminho do diretório baseado na ctegoria e no ano
    directory.mkdir(parents=True, exist_ok=True) # Cria o diretório se ele não existir    
    for item in data: # Para cada item na lista de dados
        item_id = item['url'].split('/')[-2] # Extrai o ID do item a partir da URL
        filename = directory / f"{item_id}.json" # Define o nome do arquivo .json
        with open(filename, 'w', encoding='utf-8') as f: # Abre o arquivo para escrita
            json.dump(item, f, ensure_ascii=False, indent=4) # Salva o item no arquivo JSON com formatação

# Função principal que executa o script.
def main():
    for category in ['people','films','vehicles']: # Para cada categoria de interesse
        data = fetch_all_data_from_endpoint(category) # Coleta dados da categoria
        for item in data: # Para cada item nos dados coletados
            created_year = item['created'][:4] # Extrai o ano da propriedade 'created'
            save_json([item], created_year, category) # Salva o item em um arquivo JSON dentro do diretório organizado por ano
    print('Diretórios carregados.')
    # Contando arquivos em cada diretório
    for categoria, caminho in categorias.items():
        # A função glob('*.json') retorna uma lista de todos os arquivos .json no diretório
        quantidade = len(list(caminho.glob('*.json')))
        print(f"{categoria}: {quantidade} registros")
    with open('results/registros_categorias.csv', mode='w', newline='', encoding='utf-8') as file:  # Abre/cria o arquivo CSV.
        writer = csv.writer(file)  # Cria um objeto writer para escrever no arquivo.
        writer.writerow(['datetime', 'categoria_nome', 'qtde_registros'])  # Escreve o cabeçalho do CSV.
        for categoria, caminho in categorias.items():  # Para cada categoria...
            quantidade = len(list(caminho.glob('*.json')))  # Conta o número de arquivos JSON.
            writer.writerow([datetime.now(), categoria, quantidade])  # Escreve uma linha no CSV com os dados.
        print('Arquivo .CSV criado.')

# Definindo os caminhos dos diretórios
categorias = {
    'people': Path(r"people/2014"),
    'films': Path(r"films/2014"),
    'vehicles': Path(r"vehicles/2014"),
}

# execução
if __name__ == "__main__":
    main() # Executa o script