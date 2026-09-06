aceitos = 0
soma_divisiveis = 0
print("--- GERADOR DE CÓDIGOS DIVISÍVEIS POR 3 ---")
while aceitos < 10:
    codigo = int(input(f"Informe o {aceitos + 1}º código válido: "))
    
    if codigo % 3 == 0:
        soma_divisiveis += codigo
        aceitos += 1
    else:
        print("Código rejeitado. O número deve ser divisível por 3.")

print(f"\n10 códigos aceitos com sucesso! A soma deles é: {soma_divisiveis}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO