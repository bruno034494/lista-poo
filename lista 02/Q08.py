notas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
notas_aprovadas = [
    elemento for elemento in notas
         if elemento >= 7
]
imprimir = len(notas_aprovadas)
print(f"Total de estudantes aprovados: {imprimir}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO