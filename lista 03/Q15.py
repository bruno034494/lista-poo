soma = 0
quantidade = 0
for i in range(1, 20):
    if i % 2 == 0:  # Verifica se é par
        soma += i
        quantidade += 1
media = soma / quantidade
print(f"A média dos identificadores pares (>0 e <20) é: {media:.2f}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO