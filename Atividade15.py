import random

def jogo_pedra_papel_ou_tesoura(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate"
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
        return "Jogador 1 vence"
    else:
        return "Jogador 2 vence"

def jogador_contra_computador():
    opcoes = ["pedra", "papel", "tesoura"]
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    computador = random.choice(opcoes)
    
    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")
    
    resultado = jogo_pedra_papel_ou_tesoura(jogador, computador)
    print(resultado)

def jogador_vs_jogador():
    jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
    jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()
    
    resultado = jogo_pedra_papel_ou_tesoura(jogador1, jogador2)
    print(resultado)

print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
print("1. Jogador vs Computador")
print("2. Jogador vs Jogador")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    jogador_vs_computador()
elif opcao == "2":
    jogador_vs_jogador()
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
