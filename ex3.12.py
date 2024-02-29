soma = 0
for numero in range(2,101):
    primo = True
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
            soma += numero
            break
    if primo:
        print(soma)