import random

def gerar_cartao_visa():
    primeiro_digito = 4
    numero = [primeiro_digito] + [random.randint(0, 9) for _ in range(15)]
    return ''.join(map(str, numero))

def gerar_cartao_mastercard():
    primeiro_digit = 5
    segundo_digit = random.randint(1, 5)
    numero = [primeiro_digit, segundo_digit] + [random.randint(0, 9) for _ in range(14)]
    return ''.join(map(str, numero))

def gerar_cartao_american_express():
    primeiro_digits = 3
    segundo_digits = random.choice([4, 7])
    numero = [primeiro_digits, segundo_digits] + [random.randint(0, 9) for _ in range(13)]
    return ''.join(map(str, numero))

print("Gerador de Cartão de Crédito")
print("1. Visa")
print("2. Mastercard")
print("3. American Express")

escolha = input("Escolha a empresa de cartão de crédito: ")

if escolha == "1":
    cartao = gerar_cartao_visa()
elif escolha == "2":
    cartao = gerar_cartao_mastercard()
elif escolha == "3":
    cartao = gerar_cartao_american_express()
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

print(f"Número do cartão gerado: {cartao}")
