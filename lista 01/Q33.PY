vetor = []
soma = 0
for i in range(4):
    notas = input(f"Qual é o seu elemento {i + 1}: ")
    vetor.append(notas)
menor_numero = min(vetor)
print("seu menor numero",menor_numero)