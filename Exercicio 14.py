dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print("Data inválida!")
else:
   
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:  # fevereiro
        if bissexto:
            max_dias = 29
        else:
            max_dias = 28

    if dia < 1 or dia > max_dias:
        print("Data inválida!")
    else:
        print("Data válida!")
