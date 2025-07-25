import unicodedata
import re

def ehPalindromo(x): 
    xNorm = normalizar_texto(x)
    return "Sim" if xNorm == ''.join(reversed(xNorm)) else "Não"

def remover_acentos(x): return unicodedata.normalize('NFD', x).encode('ascii', 'ignore').decode('utf-8')
def remover_pontuacao(x): return re.sub(r'[^\w\s]', '', x)
def remover_espacos(x): return re.sub(r'\s+', '', x)

def normalizar_texto(x):
    x = x.lower()
    x = remover_acentos(x)
    x = remover_pontuacao(x)
    x = remover_espacos(x)
    return x

x = input("Digite a palavra ou frase: ").lower()
print(f"\n'{x}' é palídromo? {ehPalindromo(x)}")

