texto= input("Digite uma frase: ")
palavra_presente= input("Digite uma palavra existente na frase: ")
palavra_inexistente= input("Digite uma palavra inexistente na frase: ")

novo_texto = texto.replace(palavra_presente, palavra_inexistente)
print(novo_texto)