palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
tamanho = list(map(len, palavras))
print(f"tamanho das palavras: {tamanho}")