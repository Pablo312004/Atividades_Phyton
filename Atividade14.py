import random

def gerador_de_respostas():
    respostas = ["Sim", "Não", "Talvez"]
    return random.choice(respostas)

pergunta = input("Faça uma pergunta: ")
resposta = gerador_de_respostas()
print(f"Resposta: {resposta}")
