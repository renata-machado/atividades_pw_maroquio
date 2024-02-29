chaves = input("Digite uma lista de chaves separadas por espaço: ").split()
valores = input("Digite uma lista de valores separados por espaço: ").split()
dicionario = dict(zip(chaves, valores))
print( dicionario)
