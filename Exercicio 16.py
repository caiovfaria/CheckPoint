dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Data inválida!")
else:
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        print("Áries")
    
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        print("Touro")
    
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        print("Gêmeos")
    
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        print("Câncer")
    
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        print("Leão")
    
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        print("Virgem")
    
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print("Libra")
    
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        print("Escorpião")
    
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        print("Sagitário")
    
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        print("Capricórnio")
    
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        print("Aquário")
    
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        print("Peixes")
    
    else:
        print("Data inválida!")
