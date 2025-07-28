import requests

def gerarUserAleatorio():
    url = "https://randomuser.me/api/"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            user = dados['results'][0]

            nome = f'{user["name"]["first"]} {user["name"]["last"]}'
            email = user["email"]
            pais = user["location"]["country"]

            print("Usuário Aleatório Gerado:")
            print("Nome:", nome)
            print("E-mail:", email)
            print("País:", pais)
        else:
            print("Erro na API:", response.status_code)
    
    except requests.exceptions.RequestException as erro:
        print("Erro de conexão:", erro)

gerarUserAleatorio()
