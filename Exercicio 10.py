x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))


if x == 0 and y == 0:
    print("O ponto está na origem.")


elif x == 0:
    print("O ponto está sobre o eixo Y.")

elif y == 0:
    print("O ponto está sobre o eixo X.")


elif x > 0 and y > 0:
    print("Quadrante Q1")

elif x < 0 and y > 0:
    print("Quadrante Q2")

elif x < 0 and y < 0:
    print("Quadrante Q3")

elif x > 0 and y < 0:
    print("Quadrante Q4")
