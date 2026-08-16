pu = float(input("Digite o preço unitário: "))
q = int(input("Digite a quantidade: "))
d = float(input("Digite o desconto em (R$): "))
total = pu * q
total = total - d
print(f"O valor total da compra é: R${total:.2f}")
print(f"O valor do desconto é: R${d:.2f}")
#CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO