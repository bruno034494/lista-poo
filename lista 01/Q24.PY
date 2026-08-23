soma = 0
qtd = 0
for i in range(5):
    valor = float(input("Digite um valor: "))
    if 0 < valor < 1000:
        soma += valor
        qtd += 1
if qtd > 0:
    print(f"A média é: {soma / qtd:.2f}")
else:
    print("Nenhuma medição válida.")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO