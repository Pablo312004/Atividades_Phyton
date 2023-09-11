def conversor_moeda(valor, taxa_cambio):
    return valor * taxa_cambio

moeda_de_origem = input("Digite a moeda de origem: ")
moeda_de_destino = input("Digite a moeda de destino: ")

moeda_de_origem = moeda_de_origem.upper()
moeda_de_destino = moeda_de_destino.upper()

# Verifique se as moedas são suportadas
moedas_suportadas = ["USD", "EUR", "GBP", "JPY", "CAD"]
if moeda_de_origem not in moedas_suportadas or moeda_de_destino not in moedas_suportadas:
    print("Desculpe, uma das moedas especificadas não é suportada.")
else:
    try:
        taxa_cambio = float(input(f"Digite a taxa de câmbio de {moeda_de_origem} para {moeda_de_destino}: "))
        valor_a_se_converter = float(input(f"Digite a quantidade de {moeda_de_origem} que deseja converter: "))

        valor_convertido = conversor_moeda(valor_a_se_converter, taxa_cambio)

        print(f"{valor_a_se_converter} {moeda_de_origem} é igual a {valor_convertido} {moeda_de_destino}.")
    except ValueError:
        print("Certifique-se de inserir valores numéricos válidos para a taxa de câmbio e a quantidade.")
