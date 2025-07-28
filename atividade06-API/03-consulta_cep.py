import requests

def getCEP(): return input("Digite o CEP desejado: ")
def cleanCEP(cepInit): return ''.join(filter(str.isdigit, cepInit))

def fetchAdress(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            print("CEP não encontrado!")
        else:
            print("Endereço encontrado: ")
            print(f"Logradouro: {data.get('logradouro')}")
            print(f"Bairro: {data.get('bairro')}")
            print(f"Cidade: {data.get('localidade')}")
            print(f"Estado: {data.get('uf')}")
    else:
        print("Erro na requisição.")

cep = getCEP()
cleanCep = cleanCEP(cep)

if len(cleanCep) == 8:
    fetchAdress(cleanCep)
else:
    print("CEP inválido. Digite exatamente 8 dígitos")

