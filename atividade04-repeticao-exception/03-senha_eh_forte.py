def temNumero(p):
    for char in p:
        if char.isdigit(): # isdigit() -> verifica se tem núm
            return True
    return False

while True:
    try:
        password = (input("Digite a senha a ser verificada (ou 'sair' para encerrar): "))
        if password.lower() == "sair":
            break
        if len(password) < 8:
            raise ValueError("Senha fraca: a senha deve ter ao menos 8 caracteres")
        if not temNumero(password):
            raise ValueError("Senha fraca: a senha deve ter ao menos 1 número")
        print("Senha forte!")
        break

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")