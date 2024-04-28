class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


pessoa1 = Pessoa("Renata", 18)
pessoa2 = Pessoa("Savio",20)


pessoa1.mostrar_dados()
print()
pessoa2.mostrar_dados()
