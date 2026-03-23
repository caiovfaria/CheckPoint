idade = int(input("Digite sua idade: "))
idade_contribuicao = int(input("Digite o número de anos de contribuição: "))

if idade >= 65 or idade_contribuicao >= 30:
    print("Você pode se aposentar.")
elif idade >= 60 and idade_contribuicao >= 25:
    print("Você pode se aposentar, mas com regras especiais.")
else:
    print("Você ainda não pode se aposentar.")