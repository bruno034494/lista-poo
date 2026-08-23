variacao = float(input("Digite a variação de temperatura registrada (°C): "))
if variacao < 0:
    magnitude = variacao * -1
else:
    magnitude = variacao
print(f"A magnitude da diferença de temperatura é: {magnitude:.2f} °C")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO