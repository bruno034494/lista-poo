sair = "1"

while sair == "1":
    ano = float(input("qual eh seu ano "))
    if ano % 400 == 0 and not ano % 4 == 0:
        print("O número é divisível por 400")
    else:
        print("não eh bissexto")
    sair = input("vc deseja sair aperte 0 se não aperte 1:")
#CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO    
