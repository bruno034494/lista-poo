tipo = input("qual eh o tipo de operacao? (soma= +, subtracao= -, multiplicacao= *, divisao= /) ")
n1 = float(input("qual eh seu numero 1? "))
n2 = float(input("qual eh seu numero 2? "))

if tipo == "+":
    resultado = n1 + n2
elif tipo == "-":
    resultado = n1 - n2
elif tipo == "*":
    resultado = n1 * n2
elif tipo == "/":
    resultado = n1 / n2

print(f"O resultado da operação é: {resultado:.2f}")