mes = int(input("Digite um número de 1 a 12: "))

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        match mes:
            case 1:
                nome = "Janeiro"
            case 3:
                nome = "Março"
            case 5:
                nome = "Maio"
            case 7:
                nome = "Julho"
            case 8:
                nome = "Agosto"
            case 10:
                nome = "Outubro"
            case 12:
                nome = "Dezembro"
        
        print(f"{nome} tem 31 dias")

    case 4 | 6 | 9 | 11:
        match mes:
            case 4:
                nome = "Abril"
            case 6:
                nome = "Junho"
            case 9:
                nome = "Setembro"
            case 11:
                nome = "Novembro"
        
        print(f"{nome} tem 30 dias")

    case 2:
        print("Fevereiro tem 28 ou 29 dias")

    case _:
        print("Mês inválido!")
