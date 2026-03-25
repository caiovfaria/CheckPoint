dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

match mes:
    case 2:
        limite = 29 if bissexto else 28
    case 4 | 6 | 9 | 11:
        limite = 30
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        limite = 31
    case _:
        limite = -1

print("Data válida!" if 1 <= dia <= limite else "Data inválida!")
