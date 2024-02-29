nome_produto = (input ("Digite o nome do produto: "))
preco_de_custo = float(input("Digite o preço de custo: "))
preco_de_venda = float(input("Digite o preço de venda: "))
estoque = int(input("Digite a quantidade de estoque: "))

lucro = (preco_de_venda - preco_de_custo) * estoque

print ("O lucro é: ", lucro)
