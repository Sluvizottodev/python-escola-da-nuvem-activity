def ehBissexto(ano):
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return "é bissexto"
    else:
        return "não é bissexto"
    

ano = int(input("Digite o ano: "))
print("O ano", ano, ehBissexto(ano))