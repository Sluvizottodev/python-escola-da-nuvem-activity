def conversorDolar(r): return r / 5.20
def conversorEuro(r): return r / 6.15

real = 100.00

print(f"A conversão para Dólar é: US$ {conversorDolar(real):.2f}")

print(f"A conversão para Euro é: € {conversorEuro(real):.2f}")