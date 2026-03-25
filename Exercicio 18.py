valor = float(input("Digite o valor em Reais (R$): "))

print("\nEscolha a moeda para conversão:")
print("1 - Dólar (USD)")
print("2 - Euro (EUR)")
print("3 - Libra (GBP)")
print("4 - Iene (JPY)")

opcao = int(input("Opção: "))

match opcao:
    case 1:
        taxa = 5.00 
        convertido = valor / taxa
        print(f"Valor em Dólar: ${convertido:.2f}")
    
    case 2:
        taxa = 5.40 
        convertido = valor / taxa
        print(f"Valor em Euro: €{convertido:.2f}")
    
    case 3:
        taxa = 6.20 
        convertido = valor / taxa
        print(f"Valor em Libra: £{convertido:.2f}")
    
    case 4:
        taxa = 0.035 
        convertido = valor / taxa
        print(f"Valor em Iene: ¥{convertido:.2f}")
    
    case _:
        print("Opção inválida!")
