
latencias = []
for i in range(1, 11):
    tempo = float(input(f"Informe a {i}ª latência (ms): "))
    latencias.append(tempo)

print(f"\nA menor latência registrada foi: {min(latencias)} ms")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO