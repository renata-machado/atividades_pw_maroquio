frase = input("Digite uma frase: ")
def contar_palavras(frase):
    palavras = frase.split()
    contador_o = 0
    contador_a = 0
    for palavra in palavras:
        if palavra.lower().endswith("o"):
            contador_o += 1
        elif palavra.lower().endswith("a"):
            contador_a += 1
    return contador_o, contador_a
contagem_o, contagem_a = contar_palavras(frase)
print(f"Palavras terminadas com 'o': {contagem_o}")
print(f"Palavras terminadas com 'a': {contagem_a}")