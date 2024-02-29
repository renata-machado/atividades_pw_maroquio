numero = float(input("Digite um número: "))
string = str(numero)

if string.endswith('.0'):
    print("É um número real!")
else:
    print("Não é um número real!")

