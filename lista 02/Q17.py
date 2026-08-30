d = {}
for i in range(3):
    nome = input("Qual é o nome? ") 
    numero = input("Qual é o número? ") 
    d[nome] = numero  
nome_busca = input("Digite o nome que deseja buscar: ")
if nome_busca in d:
    print(f"Seu número é {d[nome_busca]}")
else:
    print("Contato não existente!")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO