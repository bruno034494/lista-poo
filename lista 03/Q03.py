qtd_adequados = 0
qtd_lentos = 0
soma_latencias = 0
maior_latencia = 0

print("--- ANÁLISE DE CONEXÃO DO LABORATÓRIO ---")
for i in range(1, 11):
    tempo = float(input(f"Informe a latência do teste {i} (em ms): "))
    soma_latencias += tempo
    if tempo > maior_latencia:
        maior_latencia = tempo
    if tempo <= 100:
        qtd_adequados += 1
    else:
        qtd_lentos += 1
media = soma_latencias / 10

print("\n--- RESULTADOS FINAIS ---")
print(f"Testes adequados (<= 100 ms): {qtd_adequados}")
print(f"Testes lentos (> 100 ms): {qtd_lentos}")
print(f"Média das latências: {media:.2f} ms")
print(f"Maior latência registrada: {maior_latencia} ms")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO