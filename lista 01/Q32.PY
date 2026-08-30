peso = float(input("qual é seu peso?"))
altura = float(input("qual eh sua altura"))
imc = peso/(altura**2)
if imc < 18.5:
    print("abaixo do peso")
elif imc <= 18.5 and imc <= 25:
    print("peso normal")
elif imc >= 30:
    print("obesidade")
#CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO