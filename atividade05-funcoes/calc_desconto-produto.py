def calcDesconto(v, p): return v * (1.0 - (p/100))

val = float(input("Digite o valor do produto: "))
percent = int(input("Digite o percentual de desconto (ex: 10, 15, 20): "))

print(f"O valor final da compra de R$ {val:.2f} com {percent}% é de: {calcDesconto(val,percent):.2f}")