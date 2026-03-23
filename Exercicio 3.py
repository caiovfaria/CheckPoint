print("Escolha uma opção:")
print("1 - À vista no PIX")
print("2 - Cartão de crédito 1x")
print("3 - Cartão de crédito parcelado")
# aplique 10% de desconto para PIX, preço original para crédito e 5% de juros para parcelado
opcao = int(input("Digite o número da opção escolhida: "))
preco_original = float(input("Digite o preço original do produto: "))
if opcao == 1:
    preco_final = preco_original * 0.9  # 10% de desconto
    print(f"Preço final com desconto para PIX: R${preco_final:.2f}")
elif opcao == 2:
    preco_final = preco_original  # preço original para crédito
    print(f"Preço final para cartão de crédito 1x: R${preco_final:.2f}")
elif opcao == 3:
    preco_final = preco_original * 1.05  # 5% de juros para parcelado
    print(f"Preço final com juros para cartão de crédito parcelado: R${preco_final:.2f}")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")