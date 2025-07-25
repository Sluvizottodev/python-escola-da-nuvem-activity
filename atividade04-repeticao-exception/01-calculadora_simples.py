class DivisaoPorZeroException(Exception): pass
class OperacaoInvalidaException(Exception): pass

def calcSoma(x, y): return x + y
def calcSubtr(x, y): return x-y
def calcMulti(x, y): return x*y
def calcDiv(x, y):     
    if y == 0:
        raise DivisaoPorZeroException("Não é possível dividir por zero.")
    return x / y

op = int(input("Qual o operação matemática você deseja? (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão)"))
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

try:
    if op == 1: 
        print(f" A soma de {x} e {y} é {calcSoma(x,y)}")
    elif op ==2: 
        print(f"A subtração de {x} e {y} é {calcSubtr(x,y)}")
    elif op == 3: 
        print(f"A multiplicação de {x} e {y} é {calcMulti(x,y)}")
    elif op == 4: 
        print(f"A divisão de {x} e {y} é {calcDiv(x,y)}")
    else: 
        raise OperacaoInvalidaException("Código de operação inválido.")
except DivisaoPorZeroException as e:
    print(f"Erro: {e}")
except OperacaoInvalidaException as e:
    print(f"Erro: {e}")