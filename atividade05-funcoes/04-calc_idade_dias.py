import datetime

def calcIdade(a):
    return datetime.datetime.now().year - a
def anoEmDias(a): return 365 * calcIdade(a)

while True:
    try:
        ano_nascimento = int(input("Qual ano você nasceu? "))
        if ano_nascimento <= 0 or ano_nascimento > datetime.datetime.now().year:
            raise ValueError("Ano inválido!")
        break
    except ValueError:
        print(f"Digite um valor válido entre 1 e ano atual.")
# resultado aproximado visto que só considera dia
print(f"A idade em dias (considerando só o ano de nascimento) é de: {anoEmDias(ano_nascimento)} dias")
    