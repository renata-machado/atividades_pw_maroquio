distancia = float(input("digite a distância de um objeto em queda livre (m): "))
velocidade0 = float(input("digite a velocidade inicial de um objeto em queda livre (m/s²): "))

tempo = (0 + velocidade0 - distancia)

t= tempo / 5
t_quadrado= t**2

print(f"O tempo é: {t_quadrado}s")