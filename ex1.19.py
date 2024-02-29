velocidade_inicial = float(input("Digite a velocidade inicial (km/h):"))
velocidade_final = float(input("Digite a velocidade final (km/h):"))
tempo_transicao = float(input("Digite o tempo de transição entre as velocidades (s):"))

velocidade_inicial_ms = velocidade_inicial * 1000 / 3600
velocidade_final_ms = velocidade_final * 1000 / 3600
aceleracao = (velocidade_final_ms - velocidade_inicial_ms) / tempo_transicao
print(f"A aceleração é de {aceleracao:.2f} m/s²")
