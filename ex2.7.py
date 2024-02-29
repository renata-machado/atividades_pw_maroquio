numero = float(input("Digite um número: "))
string = str(numero)

if string.endswith('.0') or '.' not in string:
    print("É um número inteiro!")
else:
    print("Não é um número inteiro!")