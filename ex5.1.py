import math
numeros = list(range(21))
raiz = [math.sqrt(x) for x in numeros if x % 2 == 0]
print(raiz) 