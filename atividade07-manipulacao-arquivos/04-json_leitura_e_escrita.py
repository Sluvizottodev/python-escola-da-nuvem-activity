import json

pessoa = {
    "nome": "Mauricio",
    "idade": 25,
    "cidade": "Manaus"
}

nomeArquivo = input("Digite o nome do arquivo JSON (sem extensão): ") + ".json"

# escrita
try:
    with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")

# leitura
try:
    with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)
        print(f"Dados carregados do JSON: {conteudo}")
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
