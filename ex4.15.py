frase = input("Digite uma frase: ")

palavras = frase.split()

contagem_palavras = {}

for palavra in palavras:
    palavra_sem_pontuacao = palavra.strip(".,!?;:\"'")

    contagem_palavras[palavra_sem_pontuacao.lower()] = contagem_palavras.get(palavra_sem_pontuacao.lower(), 0) + 1

print("Contagem de cada palavra na frase:")
for palavra, contagem in contagem_palavras.items():
    print(f"{palavra}: {contagem}")