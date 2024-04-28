class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} emite um som genérico.")

class Passarinho(Animal):
    def emitir_som(self):
        print(f"{self.nome} faz 'tiu tiu'.")

passarinho = Passarinho(nome="savio")

passarinho.emitir_som()
