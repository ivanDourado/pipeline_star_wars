import json  # Importa o módulo json para ler e escrever dados em formato JSON.
import os  # Importa o módulo os que fornece uma forma portátil de usar funcionalidades dependentes do sistema operacional.
from pathlib import Path  # Importa a classe Path do módulo pathlib para manipulação de caminhos de sistema de arquivos.

def generate_results_json():
    # Define os caminhos para as pastas que contêm os dados das pessoas e filmes.
    people_path = Path(r"people/2014")
    films_path = Path(r"films/2014")

    # Inicializa uma lista vazia para armazenar os resultados finais.
    results = []

    # Itera sobre cada arquivo JSON na pasta people de 2014.
    for people_file in people_path.glob('*.json'):
        # Abre o arquivo JSON da pessoa atual e carrega os dados.
        with open(people_file, 'r', encoding='utf-8') as file:
            person_data = json.load(file)
            # Cria um dicionário para armazenar dados da pessoa com chaves específicas.
            person_dict = {
                "name": person_data["name"],  # O nome da pessoa.
                "height": person_data["height"],  # A altura da pessoa.
                "gender": person_data["gender"],  # O gênero da pessoa.
                "titles": []  # Uma lista para armazenar os títulos dos filmes.
            }
            # Itera sobre cada URL de filme na lista de filmes da pessoa.
            for film_url in person_data["films"]:
                # Extrai o ID do filme da URL.
                film_id = film_url.split('/')[-2]
                # Cria um caminho para o arquivo JSON do filme correspondente.
                film_file = films_path / f"{film_id}.json"
                # Verifica se o arquivo do filme existe.
                if film_file.exists():
                    # Abre o arquivo do filme e carrega os dados.
                    with open(film_file, 'r', encoding='utf-8') as f:
                        film_data = json.load(f)
                        # Adiciona o título do filme à lista de títulos da pessoa.
                        person_dict["titles"].append(film_data["title"])
            # Adiciona o dicionário da pessoa à lista de resultados.
            results.append(person_dict)
    #teste ok
    #print(results)
    # Cria um objeto final com uma chave "results" que contém a lista de pessoas e seus filmes.
    final_object = {"results": results}

    # cria o arquivo 'results.json' e escreve os dados no formato JSON.
    # Especifica o caminho para salvar o arquivo 'results2.json' em '/opt/airflow'.
    output_path = r'results/results2.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_object, f,ensure_ascii=False, indent=4)

# executa função
if __name__ == "__main__":
    generate_results_json()