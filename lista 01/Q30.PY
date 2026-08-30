suanota = float(input("Digite sua nota: "))
if suanota < 0 or suanota > 10:
    print("Nota inválida")
elif suanota >= 7 and suanota <= 10:
    print("Aprovado")
elif suanota > 4 and suanota < 7:
    print("Recuperação")
elif suanota < 5 and suanota >= 0:
    print("Reprovado")
#CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO