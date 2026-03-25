valor = int(input("Digite o valor do saque: "))

if valor < 2 or valor in [1, 3]:
    print("Valor inválido! Não é possível sacar esse valor com as notas disponíveis.")
else:
    n100 = valor // 100
    valor = valor % 100

    n50 = valor // 50
    valor = valor % 50

    n20 = valor // 20
    valor = valor % 20

    n10 = valor // 10
    valor = valor % 10

    n5 = valor // 5
    valor = valor % 5

    n2 = valor // 2
    valor = valor % 2

    if valor != 0:
        print("Valor inválido! Não é possível formar esse valor com as notas disponíveis.")
    else:
        print("Notas entregues:")
        print("100:", n100)
        print("50:", n50)
        print("20:", n20)
        print("10:", n10)
        print("5:", n5)
        print("2:", n2)
