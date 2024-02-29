entrada_usuario = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(float, entrada_usuario.split()))

quadrados = list(map(lambda x: x**2, numeros))

print("Lista original:", numeros)
print("Quadrados:", quadrados)