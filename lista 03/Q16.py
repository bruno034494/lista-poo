num1 = int(input("Informe o limite 1 do intervalo: "))
num2 = int(input("Informe o limite 2 do intervalo: "))

inicio = min(num1, num2)
fim = max(num1, num2)
multiplos7 = 0

for i in range(inicio, fim + 1):
    if i % 7 == 0:
        multiplos7 += 1
print(f"Quantidade de códigos múltiplos de 7 no intervalo: {multiplos7}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO