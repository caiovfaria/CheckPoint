def calcular_pedagio(tipo_veiculo):
    if tipo_veiculo == 1:
        return 5.00  # Moto
    elif tipo_veiculo == 2:
        return 10.00  # Carro
    elif tipo_veiculo == 3:
        return 15.00  # Caminhonete
    elif tipo_veiculo == 4:
        return 25.00  # Caminhão
    else:
        return 0  # Tipo inválido

def main():
    print("=== Sistema de Pedágio ===")
    print("Escolha o tipo de veículo:")
    print("1 - Moto")
    print("2 - Carro")
    print("3 - Caminhonete")
    print("4 - Caminhão")

    try:
        tipo = int(input("Digite o número do veículo: "))
        valor = calcular_pedagio(tipo)

        if valor == 0:
            print("Tipo de veículo inválido!")
        else:
            print(f"Valor do pedágio: R$ {valor:.2f}")
    except ValueError:
        print("Entrada inválida! Digite apenas números.")

# Executa o programa
main()