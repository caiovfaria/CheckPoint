import math

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A == 0:
    print("Não é uma equação do segundo grau.")
else:
    delta = B**2 - 4*A*C
    print("Delta =", delta)

    if delta < 0:
        print("Não há raízes reais.")
    
    elif delta == 0:
        x = -B / (2*A)
        print("Raiz única:", x)
    
    else:
        x1 = (-B + math.sqrt(delta)) / (2*A)
        x2 = (-B - math.sqrt(delta)) / (2*A)
        print("Duas raízes reais:")
        print("x1 =", x1)
        print("x2 =", x2)
