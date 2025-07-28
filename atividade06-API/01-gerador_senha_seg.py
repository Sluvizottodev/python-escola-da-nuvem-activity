import random
import string

def get_password_length():
    return int(input("Tamanho de senha desejado: "))

def complete_password(password, total_length, all_chars):
    while len(password) < total_length:
        password.append(random.choice(all_chars))
    return password

pLength = get_password_length()

lUpperCase = string.ascii_uppercase
lLowerCase = string.ascii_lowercase
number = string.digits
symbol = string.punctuation

password = [
    random.choice(lUpperCase),
    random.choice(lLowerCase),
    random.choice(number),
    random.choice(number),
    random.choice(symbol)
]

randomChar = lUpperCase + lLowerCase + number + symbol

password = complete_password(password, pLength, randomChar)
random.shuffle(password)

passwordFinal = ''.join(password)
print(f"Senha gerada: {passwordFinal}")
