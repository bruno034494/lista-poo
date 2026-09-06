num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

menor = min(num1, num2)
maior = max(num1, num2)

print(f"\n--- INTERVALO ENTRE {menor} E {maior} ---")
for i in range(menor, maior + 1):
    print(i)
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO