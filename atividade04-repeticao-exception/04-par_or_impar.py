def ehPar(n):
    return "par" if n % 2 == 0 else "ímpar"

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar)")
    if entrada.lower() == "fim": break

    try:
        n = int(entrada)
        res = ehPar(n)
        print("O número digitado é:", res)
        if res == "par": pares+=1
        else: impares+=1
    except:
        print("Entrada inválida")

print(f"\nPares: {pares} | Ímpares: {impares}")
