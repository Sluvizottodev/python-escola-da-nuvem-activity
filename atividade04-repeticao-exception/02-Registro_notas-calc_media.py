def media(n):
    if len(n) > 0:
        return sum(n) / len(n)
    return 0

n = []
qtd = 0
while True:
    typed= input("Digire um número entre 0 e 10 (ou fim para encerrar programa): ")
    if typed.lower() == "fim":
        break

    try:
        nota = float(typed)
        if 0 <= nota <= 10:
            n.append(nota)
        else: print("Número foraa do intervalo. Digite entre 0-10.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

print(f"\nTotal de notas válidas: {len(n)}")
print(f"Média da turma: {media(n):.2f}")