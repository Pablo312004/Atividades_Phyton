import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def determinar_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    else:
        return "Peixes"

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = calcular_idade(ano_nascimento)
print(f"Sua idade é {idade} anos.")

mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))
dia_nascimento = int(input("Digite o dia de nascimento (1-31): "))

signo = determinar_signo(dia_nascimento, mes_nascimento)
print(f"Seu signo do zodíaco é {signo}.")
