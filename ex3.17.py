numeros = []

maior = 0
menor = 0
for i in range (10):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

numeros.remove(maior_numero)
numeros.remove(menor_numero)

segundo_maior_numero = max(numeros)
segundo_menor_numero = min(numeros)

print(f"O segundo maior número é: {segundo_maior_numero}")
print(f"O segundo menor número é: {segundo_menor_numero}:")