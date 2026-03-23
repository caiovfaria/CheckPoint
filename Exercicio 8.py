print("Calculadora de Imposto de Renda")

salario = float(input("Digite o valor do seu salário: "))

if salario <= 2.112:
    imposto = 0
elif salario <= 2.826:
    imposto = salario * 0.075 - 1713.58
else:
    print("Salário acima do limite para cálculo de imposto.")
