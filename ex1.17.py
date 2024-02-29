preco_mercadoria = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite a taxa de desconto (%):"))
imposto = float(input("Digite o imposto (%):"))

preco_desconto = preco_mercadoria - (preco_mercadoria * (desconto / 100))
preco_final_mercadoria = preco_desconto + (preco_desconto * (imposto / 100))
print(f"O valor final da mercadoria é de R${preco_final_mercadoria}")


 