jogador = input("Escolha Pedra, Papel ou Tesoura: ").lower()
computador = "pedra"

if jogador == computador:
    print("Empate!")
else:
    if jogador == "pedra":
        if computador == "tesoura":
            print("Você venceu!")
        else:
            print("Você perdeu!")
    
    elif jogador == "papel":
        if computador == "pedra":
            print("Você venceu!")
        else:
            print("Você perdeu!")
    
    elif jogador == "tesoura":
        if computador == "papel":
            print("Você venceu!")
        else:
            print("Você perdeu!")
    
    else:
        print("Opção inválida!")
