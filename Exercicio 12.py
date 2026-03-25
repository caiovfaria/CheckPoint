nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = float(input("Digite a porcentagem de faltas (%): "))


if faltas > 25:
    print("Reprovado por Faltas")
else:
    media = (nota1 + nota2) / 2
    print("Média:", media)

    if media >= 7.0:
        print("Aprovado")
    elif media >= 5.0:
        print("Recuperação")
    else:
        print("Reprovado por Nota")
