aluno_a = {'Python', 'Java', 'C'}
aluno_b = {'Java', 'JavaScript', 'PHP'}

print("--- ANÁLISE DE LINGUAGENS DE PROGRAMAÇÃO ---")
print(f"Linguagens informadas pelo Aluno A: {aluno_a}")
print(f"Linguagens informadas pelo Aluno B: {aluno_b}")

ambos = aluno_a & aluno_b
print(f"Linguagens conhecidas por ambos: {ambos}")

pelo_menos_um = aluno_a | aluno_b
print(f"Linguagens conhecidas por pelo menos um: {pelo_menos_um}")

apenasa = aluno_a - aluno_b
print(f"Linguagens conhecidas apenas pelo Aluno A: {apenasa}")

print(f"Quantidade de linguagens diferentes na pesquisa: {len(pelo_menos_um)}")

# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO