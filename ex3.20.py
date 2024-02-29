numero = int(input("Digite um número:"))

for num in range (1, numero + 1):
    fatorial = 1
    for i in range (1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é {fatorial}")