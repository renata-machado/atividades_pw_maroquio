class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =idade
        
    def emitir_som(self): 
        print(f"O animal {self.nome} de idade {self.idade}anos emite um som genérico")  

animal1 = Animal("vaca", 2)

animal1.emitir_som()