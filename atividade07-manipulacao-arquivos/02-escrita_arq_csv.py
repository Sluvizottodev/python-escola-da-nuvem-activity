import csv
def nomeArquivo():
    return input("Digite o nome do arquivo onde os dados serão salvos: ")

dados = [
    ["Jõao", 18, "Engenheiro Eletrônica"],
    ["Stefani", 20, "Sistemas de Informação"],
    ["Sarah", 23, "Engenharia elétrica"]
]

name = nomeArquivo()
try:
    with open(name+".csv", "w", newline = '', encoding="utf-8") as arquivo:
        e = csv.writer(arquivo)
        e.writerow(['nome', 'idade', 'curso'])
        e.writerows(dados)
    print(f"Arquivo '{name}.csv' salvo com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")