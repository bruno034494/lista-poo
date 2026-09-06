cpu = []
for i in range(7):
    valor = int(input(f"Informe a utilização da CPU no instante {i+1} (%): "))
    cpu.append(valor)
print("\n--- VALORES REGISTRADOS (ORDEM INVERSA) ---")
for valor in cpu[::-1]:
    print(f"{valor}%")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO