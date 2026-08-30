
lista_numeros = list(range(1, 11))

print("Informe as disciplinas da Licenciatura em Computação:")
lista_disciplinas = [input(f"Qual é a {i}ª disciplina? ") for i in range(1, 5)]

ano_ingresso = 2025
ano_atual = 2026
lista_anos = [ano_ingresso, ano_atual]

print("\n--- LISTAS CRIADAS ---")
print(f"a) Números: {lista_numeros}")
print(f"b) Disciplinas: {lista_disciplinas}")
print(f"c) Anos: {lista_anos}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO