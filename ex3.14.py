numero = int(input("Digite um número: "))

primo = True
for i in range(2,numero):
    if numero % i == 0:
        primo = False
        break
if primo:
    print(f"O número {numero} é primo!")
else:
     print(f"O número {numero} não é primo!")