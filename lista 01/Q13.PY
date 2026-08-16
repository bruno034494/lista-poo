soma = 0
for i in range(1, 4):
    quantidade = float(input(f"Digite a temperatura do sensor {i}: "))
    soma = soma + quantidade
media = soma / 3
print(f"A média das temperaturas dos sensores é:{media:.2f}°C")
#CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO
