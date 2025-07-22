def calcPrecoTotal(preco_uni, qtd):
    return preco_uni * qtd

nome = "Cadeira infantil"
preco_uni = 12.40
qtd = 3

print("O preço total da compra de",qtd, "unidades de", nome, "é", str(calcPrecoTotal(preco_uni,qtd)) + ".")
# transformei em string para que pudesse usar o ponto se o f-string ou deixar um espaço no fim!