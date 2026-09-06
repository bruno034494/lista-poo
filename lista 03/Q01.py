ciclo_anterior = 0
print("--- RELATÓRIO DE REQUISIÇÕES ---")

for ciclo_atual in range(10):
    soma = ciclo_atual + ciclo_anterior
    print(f"Ciclo Atual: {ciclo_atual} | Ciclo Anterior: {ciclo_anterior} | Soma: {soma}")
    ciclo_anterior = ciclo_atual
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO