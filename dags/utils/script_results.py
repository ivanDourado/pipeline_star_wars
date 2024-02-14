import json  # Importa a biblioteca para manipulação de dados JSON.
from pathlib import Path  # Importa a biblioteca para manipulação de caminhos de arquivos no sistema.

# Função que processa os arquivos dentro de um diretório especificado.
def process_files_in_directory(directory_path, films_base_path):
    results = []  # Inicializa uma lista para armazenar os resultados finais.
    # Itera sobre cada arquivo JSON no diretório especificado.
    for json_file in directory_path.glob('*.json'):
        # Abre o arquivo JSON para leitura.
        with json_file.open('r', encoding='utf-8') as file:
            person_data = json.load(file)  # Carrega os dados JSON do arquivo.
            # Cria um dicionário para armazenar informações da pessoa.
            person_dict = {
                "name": person_data["name"],  # Nome da pessoa.
                "height": person_data["height"],  # Altura da pessoa.
                "gender": person_data["gender"],  # Gênero da pessoa.
                "titles": []  # Lista para armazenar os títulos dos filmes em que a pessoa aparece.
            }
            # Itera sobre cada URL de filme na lista de filmes da pessoa.
            for film_url in person_data["films"]:
                film_id = film_url.split('/')[-2]  # Extrai o ID do filme da URL.
                # Monta o caminho para o arquivo JSON do filme, considerando o ano de criação da pessoa.
                film_file = films_base_path / person_data['created'][:4] / f"{film_id}.json"
                # Verifica se o arquivo do filme existe.
                if film_file.exists():
                    # Abre o arquivo do filme para leitura.
                    with film_file.open('r', encoding='utf-8') as f:
                        film_data = json.load(f)  # Carrega os dados JSON do filme.
                        # Adiciona o título do filme à lista de títulos da pessoa.
                        person_dict["titles"].append(film_data["title"])
            # Adiciona o dicionário da pessoa aos resultados finais.
            results.append(person_dict)
    print('Informações coletadas no formato solicitado.')
    return results  # Retorna a lista de resultados finais.

# Função principal que gera o arquivo JSON com os resultados.
def generate_results_json():
    people_base_path = Path("people")  # Caminho base para os dados das pessoas.
    films_base_path = Path("films")  # Caminho base para os dados dos filmes.
    final_results = []  # Inicializa uma lista para armazenar os resultados finais.

    # Itera sobre cada subdiretório no caminho das pessoas, representando anos diferentes.
    for year_dir in people_base_path.iterdir():
        if year_dir.is_dir():
            # Processa os arquivos no subdiretório, passando o caminho base dos filmes como argumento.
            results = process_files_in_directory(year_dir, films_base_path)
            final_results.extend(results)  # Adiciona os resultados à lista final.

    # Cria um objeto final contendo todos os resultados.
    final_object = {"results": final_results}
    # Define o caminho para salvar o arquivo de resultados.
    output_path = Path('results/results2.json')
    # Abre o arquivo para escrita, salvando os resultados no formato JSON.
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(final_object, f, ensure_ascii=False, indent=4)
    print('Arquivo results2 criado no formato pedido.')

# Executa a função principal se o script for o principal executado.
if __name__ == "__main__":
    generate_results_json()
