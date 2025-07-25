def calcGorjeta(v,p):
    return v * (p/100)

percent = int(input("Digite a porcentagem (%) de gorjeta desejada (ex: 10, 25, 20)"))
valor_compra = 100.00

print(f"O valor da gorjeta para a compra de R$ {valor_compra:.2f} com base na porcentagem {percent:.2f}% é de {calcGorjeta(valor_compra,percent):.2f}")

