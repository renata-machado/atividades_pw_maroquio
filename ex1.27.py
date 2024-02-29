nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
valor_imposto = float(input("Digite o valor do imposto: "))

salario_liquido = salario - valor_imposto
print(f"O seu salário líquido é de R${salario_liquido}")