texto = input("Digite uma string: ")
letras_maiusculas = 0
letras_minusculas = 0
digitos = 0
caracteres_especiais = 0
for caractere in texto:
    if caractere.isupper():
        letras_maiusculas += 1
    elif caractere.islower():
        letras_minusculas += 1
    elif caractere.isdigit():
        digitos += 1
    else:
        caracteres_especiais += 1
palavras = texto.split()
quantidade_palavras = len(palavras)
print(f"Letras maiúsculas: {letras_maiusculas}")
print(f"Letras minúsculas: {letras_minusculas}")
print(f"Dígitos: {digitos}")
print(f"Caracteres especiais: {caracteres_especiais}")
print(f"Quantidade de palavras: {quantidade_palavras}")
