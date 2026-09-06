gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 
            'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 
            'A', 'B', 'C', 'D', 'E']
respostas_aluno = []
acertos = 0
print("--- SISTEMA DE CORREÇÃO ---")
for i in range(25):
    resposta = input(f"Informe a resposta do estudante para a Questão {i+1} (A/B/C/D/E): ").upper()
    respostas_aluno.append(resposta)
    if resposta == gabarito[i]:
        acertos += 1
erros = 25 - acertos
percentual = (acertos / 25) * 100
print("\n--- RELATÓRIO DO ESTUDANTE ---")
print(f"Quantidade de acertos: {acertos}")
print(f"Quantidade de erros: {erros}")
print(f"Percentual de aproveitamento: {percentual:.2f}%")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO