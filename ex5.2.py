frase = input("Digite ums frase: ")
palavras = frase.split()
contem_a = filter(lambda p: p.find("a")>=0, palavras)
# outra maneira contem_a = filter(lambda p: "a" in p, palavras)
subst_o = [p.replace("a", "o") for p in palavras]
print(" ".join(subst_o) )


# contem_a = filter(lambda p: p.find("a")>=0, palavras) filtrar as palavras 
# contem_a = filter(lambda p: "a" in p, palavras)  filtrar as palavras
