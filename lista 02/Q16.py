d = {
    "bruno": 7,
    "natan": 8,
    "paulo": 10,
    "pablo": 9,
    "marcos": 0 
}
for chave, valor in d.items():
    if valor >= 7:
        print(f"Foi aprovado aluno: {chave}, nota: {valor}")
    else:
        print(f"Foi reprovado aluno: {chave}, nota: {valor}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO