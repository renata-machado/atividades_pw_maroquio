frase = input("Digite uma frase: ")
artigos = ["o", "a", "os", "as", "um", "uma", "uns", "umas"]
palavras = frase.split()
palavras_sem_artigos = [palavra for palavra in palavras if palavra.lower() not in artigos]
frase_sem_artigos = " ".join(palavras_sem_artigos)
print("Frase sem artigos:", frase_sem_artigos)