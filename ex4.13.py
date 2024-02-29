frase = input("Digite uma frase: ")
palavras = frase.split()
palavras_sem_espacos = [palavra.strip() for palavra in palavras]
frase_com_um_espaco = " ".join(palavras_sem_espacos)
print(frase_com_um_espaco)