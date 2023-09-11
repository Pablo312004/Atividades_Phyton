def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temp = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade (C para Celsius, F para Fahrenheit): ").upper()
if unidade == "C":
    fahrenheit = celsius_para_fahrenheit(temp)
    print(f"{temp}°C é igual a {fahrenheit}°F.")
elif unidade == "F":
    celsius = fahrenheit_para_celsius(temp)
    print(f"{temp}°F é igual a {celsius}°C.")
else:
    print("Unidade inválida.")
