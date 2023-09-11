import random
import string

def gerador_de_senha(comprimento, letras, numeros, especiais):
    if letras + numeros + especiais > comprimento:
        print("A soma das letras, números e caracteres especiais não pode ser maior que o comprimento da senha.")
        return None

    caracteres = ""

    if letras > 0:
        caracteres += string.ascii_letters

    if numeros > 0:
        caracteres += string.digits

    if especiais > 0:
        caracteres += string.punctuation

    if not caracteres:
        print("Selecione pelo menos um tipo de caractere para gerar a senha.")
        return None

    senha_desejada = ''.join(random.choice(caracteres) for _ in range(comprimento))

    return senha

# Solicitação de entrada do usuário
comprimento_de_senha = int(input("Digite o comprimento da senha desejada: "))
quantidade_requerida_de_letras = int(input("Digite a quantidade de letras na senha: "))
quantidade_necessaria_de_numeros = int(input("Digite a quantidade de números na senha: "))
quantidade_especiais = int(input("Digite a quantidade de caracteres especiais na senha: "))

senha_gerada = gerador_de_senha(comprimento_de_senha, quantidade_requerida_de_letras, quantidade_necessaria_de_numeros, quantidade_especiais)

if senha_gerada:
    print(f"Sua senha gerada é: {senha_gerada}")
