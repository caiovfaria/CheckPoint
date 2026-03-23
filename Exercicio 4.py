print("Conversor de segundos")
tempo = int(input("Digite o valor: "))

horas = tempo // 3600
tempo = tempo % 3600
minutos = tempo // 60
tempo = tempo % 60
print(f"{horas} horas, {minutos} minutos e {tempo} segundos")