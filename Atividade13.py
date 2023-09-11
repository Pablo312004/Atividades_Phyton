calculaando_fatorial(numero):
    if numero < 0:
        return "Erro: Não é possível calcular o fatorial de um número negativo."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero = int(input(" Digite um número para calcular o fatorial, por favor: "))
resultado = calcular_fatorial(numero)
print(f" O fatorial de {numero} é {resultado}")
