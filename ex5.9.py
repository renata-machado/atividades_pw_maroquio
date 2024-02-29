entrada_usuario = input("Digite uma lista de nomes separados por espaço: ")

nomes = entrada_usuario.split()

nomes_em_caixa_alta = list(map(str.upper, nomes))

print("Lista original:", nomes)
print("Nomes em caixa alta:", nomes_em_caixa_alta)