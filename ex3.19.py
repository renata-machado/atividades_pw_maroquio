palavra = input("Digite uma palavra: ")
palindromo = palavra[::-1]
if palavra == palindromo:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")