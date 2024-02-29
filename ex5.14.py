nomes = input("Digite uma lista de nomes separados por espaço: ").split()
notas = [float(x) for x in input("Digite uma lista de notas separadas por espaço: ").split()]
tuplas_ordernadas = sorted(zip(nomes, notas), key=lambda x: x[1], reverse=True)
print(f"notas decrescentes: {tuplas_ordernadas}" )