numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)