valores = []
for i in range(1, 16):
    uso = float(input(f"Informe a utilização do processador no {i}º período (%): "))
    valores.append(uso)
print(f"\nO maior valor de utilização observado foi: {max(valores)}%")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO