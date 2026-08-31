boletim = {
    "Natan": {
        "Nota 1": 8.0,
        "Nota 2": 7.5,
        "Média": 7.75
    },
    "Bruno": {
        "Nota 1": 6.0,
        "Nota 2": 6.0,
        "Média": 6.0
    }
}
for nome, dados in boletim.items():
    print(f"Aluno: {nome}")
    print(f"Nota 1: {dados['Nota 1']}")
    print(f"Nota 2: {dados['Nota 2']}")
    print(f"Média: {dados['Média']}")
    
    if dados['Média'] >= 7.0:
        print("Situação: Aprovado\n")
    else:
        print("Situação: Reprovado\n")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO