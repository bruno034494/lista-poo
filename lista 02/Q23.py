curso1 = int(input("Quantidade de alunos do Curso 1: "))
curso2 = int(input("Quantidade de alunos do Curso 2: "))

if curso1 > curso2:
    mensagem = "O Curso 1 possui mais alunos."
elif curso2 > curso1:
    mensagem = "O Curso 2 possui mais alunos."
else:
    mensagem = "Os dois cursos possuem a mesma quantidade de alunos."
print(mensagem)

with open("dados_matriculas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Curso 1: {curso1} alunos\n")
    arquivo.write(f"Curso 2: {curso2} alunos\n")
    arquivo.write(f"Resultado: {mensagem}\n")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO