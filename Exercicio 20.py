tipo = int(input("Digite o tipo de veículo (1-4): "))

match tipo:
    case 1: #moto
        print("Valor: R$ 5.00")
    case 2: #carro
        print("Valor: R$ 10.00")
    case 3: #caminhonte
        print("Valor: R$ 15.00")
    case 4: #caminhão
        print("Valor: R$ 25.00")
    case _:
        print("Tipo inválido!")
