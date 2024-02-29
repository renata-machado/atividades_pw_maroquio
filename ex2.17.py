peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em m: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc <= 24.9:
    print("Você está com o peso normal!")
elif imc >= 25 and imc <= 29.9:
    print("Você está com sobrepeso!")
else:
    print("Você está com obedidade!")