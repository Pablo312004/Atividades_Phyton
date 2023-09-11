import datetime

def calcular_idade_em_meses():
    data_nascimento = datetime.datetime.strptime(input("Digite sua data de nascimento (YYYY-MM-DD): "), "%Y-%m-%d")
    hoje = datetime.datetime.now()
    diferenca = hoje - data_nascimento
    return diferenca.days // 30
def calcular_idade_em_dias():
    data_nascimento = datetime.datetime.strptime(input("Digite sua data de nascimento (YYYY-MM-DD): "), "%Y-%m-%d")
    hoje = datetime.datetime.now()
    diferenca = hoje - data_nascimento
    return diferenca.days
def calcular_idade_em_horas():
    data_nascimento = datetime.datetime.strptime(input("Digite sua data de nascimento (YYYY-MM-DD): "), "%Y-%m-%d")
    hoje = datetime.datetime.now()
    diferenca = hoje - data_nascimento
    return diferenca.total_seconds() / 3600
def calcular_idade_em_minutos():
    data_nascimento = datetime.datetime.strptime(input("Digite sua data de nascimento (YYYY-MM-DD): "), "%Y-%m-%d")
    hoje = datetime.datetime.now()
    diferenca = hoje - data_nascimento
    return diferenca.total_seconds() / 60
def calcular_idade_em_segundos():
    data_nascimento = datetime.datetime.strptime(input("Digite sua data de nascimento (YYYY-MM-DD): "), "%Y-%m-%d")
    hoje = datetime.datetime.now()
    diferenca = hoje - data_nascimento
    return diferenca.total_seconds()
while True:
    print("\nMenu Interativo")
    print("1. Calcular idade em meses")
    print("2. Calcular idade em dias")
    print("3. Calcular idade em horas")
    print("4. Calcular idade em minutos")
    print("5. Calcular idade em segundos")
    print("6. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print(f"Sua idade em meses é: {calcular_idade_em_meses()} meses.")
    elif escolha == "2":
        print(f"Sua idade em dias é: {calcular_idade_em_dias()} dias.")
    elif escolha == "3":
        print(f"Sua idade em horas é: {calcular_idade_em_horas()} horas.")
    elif escolha == "4":
        print(f"Sua idade em minutos é: {calcular_idade_em_minutos()} minutos.")
    elif escolha == "5":
        print(f"Sua idade em segundos é: {calcular_idade_em_segundos()} segundos.")
   
