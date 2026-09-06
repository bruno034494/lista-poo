frequencia_eventos = {}
print("--- REGISTRO DE EVENTOS ---")
for i in range(10):
    codigo = int(input(f"Informe o código do {i+1}º evento: "))
    
    if codigo in frequencia_eventos:
        frequencia_eventos[codigo] += 1
    else:
        frequencia_eventos[codigo] = 1
print("\n--- OCORRÊNCIAS DOS EVENTOS ---")
for codigo, quantidade in frequencia_eventos.items():
    print(f"Código {codigo}: ocorreu {quantidade} vez(es)")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO