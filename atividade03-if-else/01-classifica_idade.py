def classificaIdade( idade ):
    if(idade <=12 and idade >= 0 ):
        return "Criança"
    elif(idade <= 17):
        return "Adolescente"
    elif(idade <= 59):
        return "Adulto"
    elif(idade < 0):
        return "Idade inválida"
    else:
        return "Idoso"

idade = int(input("Digite sua idade: "))
print("Você tem", idade, "e é um(a)", classificaIdade(idade))