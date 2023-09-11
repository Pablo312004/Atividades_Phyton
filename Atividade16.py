def calcular_total_com_imposto(valor_compra, taxa_imposto):
    valor_do_imposto = valor_compra * (taxa_imposto / 100)
    valor_total = valor_compra + valor_do_imposto
    return valor_total

valor_compra = float(input("Digite o valor da compra: "))
taxa_do_imposto = float(input("Digite a taxa de imposto (%): "))

valor_total = calcular_total_com_imposto(valor_compra, taxa_imposto)
print(f"O valor total da compra após adicionar o imposto é: R$ {valor_total:.2f}")
