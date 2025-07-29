import csv
def nomeArquivo():
    return input("Digite o nome do arquivo csv a ser lido: ")

name = nomeArquivo()
with open(name+'.csv', 'r', newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for l in leitor:
        print(f"Linha CSV: {l}")
