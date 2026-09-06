primeiro = int(input("Informe o primeiro identificador: "))
ultimo = int(input("Informe o último identificador: "))

soma = 0
quantidade = 0

for i in range(primeiro, ultimo + 1):
    soma += i
    quantidade += 1

media = soma / quantidade
print(f"\nA média dos identificadores no intervalo é: {media:.2f}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO