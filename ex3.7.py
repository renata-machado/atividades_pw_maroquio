soma = 0
contador = 0
media = 0
numero = float(input("Digite um número: "))
while numero >= 0:
    soma += numero
    contador += 1
    numero = float(input("Digite outro número: "))
media = soma / contador
print(f"A média dos números é {media}")