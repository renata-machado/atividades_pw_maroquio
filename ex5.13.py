lista1 = [float(x) for x in input("Digite a primeira lista de números separados por espaço: ").split()]
lista2 = [float(x) for x in input("Digite a segunda lista de números separados por espaço: ").split()]
media = list(map(lambda x, y: (x + y) / 2, lista1, lista2))
print("Médias dos elementos correspondentes:", media)