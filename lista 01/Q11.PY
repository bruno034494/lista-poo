print("codigo para calcular o montante e os juros pagos no fim do periodo de um emprestimo")
c = float(input("Digite o seu capital: "))
i = float(input("Digite a taxa de juros (em %): "))
t = float(input("Digite o tempo (em meses): "))
calcularmontante = c * (1 + (i / 100) * t)
juros = calcularmontante - c
print("O valor dos juros pagos no fim do periodo:R$", juros)
print("O valor do montante pago no fim do periodo:R$", calcularmontante)
#CODIGO FEITO POR: BRUNO DE SOUZA BUENO