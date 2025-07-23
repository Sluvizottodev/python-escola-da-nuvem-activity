def calcIMC( p, a):
    return p/ (a**2)

def classificaIMC (i):
    if(i <= 0):
        return "Inválido"
    elif(i < 18.5):
        return "Abaixo do peso"
    elif(i < 25):
        return "Peso normal"
    elif(i < 30):
        return "Sobrepeso"
    else:
        return "obeso"

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura (ex: 1.60): "))
IMC = calcIMC(peso, altura)
print("Sua claddificação de IMC é:", classificaIMC(IMC))