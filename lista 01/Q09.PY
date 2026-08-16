l1 = float(input("Digite o o primeiro lado do seu triangulo: "))
l2 = float(input("Digite o o segundo lado do seu triangulo: "))
l3 = float(input("Digite o o terceiro lado do seu triangulo: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("os valores forman um triangulo ")
    if l1 == l2 and l2 == l3:
        print("O seu triangulo é equilatero!")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("O seu triangulo é isosceles!")
    else:
        print("O seu triangulo é escaleno!")
else:
    print("Os valores informados NÃO formam um triângulo.")
#CODIGO FEITO POR: BRUNO DE SOUZA BUENO