matriz = [
    [1, 2, 3],
    [4, 2, 5],
    [6, 7, 1],
    [6, 7, 1]
]
vistos = set()
repetidos = set()

for linha in matriz:
    for elemento in linha:
        if elemento in vistos:
            repetidos.add(elemento)
        else:
            vistos.add(elemento)
print(list(repetidos))
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO