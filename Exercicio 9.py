num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("Digite o número da operação: ")

if op == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif op == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif op == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif op == "4":
    if num2 == 0:
        print("Operação inválida")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)

else:
    print("Opção inválida")