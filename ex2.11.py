temperatura = float(input("Digite a temperatura: "))

if temperatura > 37:
    print("A temperatura está acima do normal!")
elif temperatura < 36:
    print("A temperatura está abaixo do normal!")
else:
    print("A temperatura está dentro da faixa normal (36°C a 37°C).")