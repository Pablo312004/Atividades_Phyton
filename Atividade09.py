def calculando_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc < 24.9:
    print("Você está dentro do peso ideal.")
else:
    print("Você está acima do peso ideal.")
