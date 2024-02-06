import requests
import pandas as pd


def fetch_swapi_data(endpoint):
    """
    Função para buscar dados da SWAPI (Star Wars API)

    Args:
    - endpoint: str. O endpoint da API a ser consultado (ex: 'people', 'planets')

    Returns: 
    - Data: dict. Os dados retornados pela API
    """
    base_url = 'https://swapi.dev/api/'
    url = f'{base_url}{endpoint}/'
    response = requests.get(url)

    if response.status_code == 200: 
        return response.json() # Retorna os dados decodificados
    else: 
        print("Falha na requisição: Status", response.status_code)
        return None

#exemplo de uso
if __name__ == "__main__":
    endpoint = 'people' # Exemplo para buscar informações sobre pessoas
    data = fetch_swapi_data(endpoint)

    if data:
        print(data) # imprime os dados coletados
    else: 
        print("Não foi possível obter dados da API.")