import requests
from datetime import datetime

def getCodMoedaEstrangeira():
    return input("Digite o código da moeda desejada (Ex: USD, EUR, GBP): ")

def fetchExchangeRate(cod):
    url = f"https://economia.awesomeapi.com.br/last/{cod}-BRL"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            key = f"{cod}BRL"
            if key in data:
                return data[key]
            else:
                print("Código de moeda inválido!")
        else:
            print("Erro na resposta da API")
    except Exception as e:
        print(f"Erro de conexão: {e}")

def displayExchangeInfo(i):
    print(f"Cotação atual:\nMoeda: {i.get('name')}, valor atual: R$ {i.get('bid')}, valor máximo: R$ {i.get('high')}, valor mínimo: R$ {i.get('low')}")
    timestamp = int(i.get('timestamp'))
    dataHora = datetime.fromtimestamp(timestamp)
    print(f"Última atualização: {dataHora.strftime('%d/%m/%Y %H:%M:%S')}")

cod = getCodMoedaEstrangeira().upper()
info = fetchExchangeRate(cod)
if info:
    displayExchangeInfo(info)
