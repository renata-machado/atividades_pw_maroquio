frase = input("Digite uma frase: ")

palavras = frase.split()

print("Posição inicial de cada palavra:")
for palavra in palavras:
    posicao = frase.find(palavra)
    print(f"{palavra}: {posicao}")