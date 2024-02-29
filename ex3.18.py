numero = int(input("Digite um número inteiro: "))
fibonacci_sequencia = [1, 1]

for i in range(2, numero):
    fibonacci = fibonacci_sequencia[i - 1] + fibonacci_sequencia[i - 2]
    fibonacci_sequencia.append(fibonacci)

print(f"Sequência de Fibonacci até o {numero}-ésimo termo:")
print(fibonacci_sequencia)