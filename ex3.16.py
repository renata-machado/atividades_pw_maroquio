numeros = []

maior = 0
menor = 0
for i in range (10):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
