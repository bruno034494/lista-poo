memoria = []
for i in range(5):
    valor = float(input(f"Informe a quantidade de memória utilizada no teste {i+1}: "))
    memoria.append(valor)
soma_total = sum(memoria)
print(f"\nA soma de todos os valores de memória registrados é: {soma_total}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO