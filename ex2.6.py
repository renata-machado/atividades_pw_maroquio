texto = "arara"
texto_invertido = texto[::-1]  # diz que vai do extremo, ou seja final ao início (de trás pra frente)
#(texto[10:3:-1]) diz que vai do nove (uma casa do limite a menos) ao três, de trás pra frente 
#(texto[0:5:2]) vai do zero ao quarto (um a menos do limite) pulando de dois em dois

if texto == texto_invertido:
    print("É um palímdromo.")
else:
    print("Não é um palímdromo.")


