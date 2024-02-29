frase = input("Digite uma frase: ")
substrings = [frase[x:x + 6] for x in range(0, len(frase), 6)]
for substring in substrings:
    print(substring)