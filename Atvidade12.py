import random

def jogo_par_ou_impar():
    print("Jogo de Par ou Ímpar")
    usuario = input("Escolha Par (P) ou Ímpar (I): ").strip().upper()
    
    if usuario not in ['P', 'I']:
        print("Escolha inválida. Digite 'P' para Par ou 'I' para Ímpar.")
        return

    numero_usuario = int(input("Digite um número entre 1 e 10: "))
    
    if numero_usuario < 1 or numero_usuario > 10:
        print("Número fora do intervalo permitido (1 a 10).")
        return

    numero_computador = random.randint(1, 10)
    soma = numero_usuario + numero_computador
    
    print(f"Você escolheu {usuario} e jogou o número {numero_usuario}.")
    print(f"O computador jogou o número {numero_computador}.")
    print(f"O total é {soma}.")
    
    if (soma % 2 == 0 and usuario == 'P') or (soma % 2 != 0 and usuario == 'I'):
        print("Você venceu!")
    else:
        print("O computador venceu!")

jogo_par_ou_impar()
