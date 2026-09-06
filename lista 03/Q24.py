estudantes = []
maior_media = -1
melhor_estudante = ""
print("--- CADASTRO DE NOTAS ---")
for i in range(10):
    nome = input(f"\nNome do {i+1}º estudante: ")
    n1 = float(input("Nota da Avaliação 1 (Peso 3): "))
    n2 = float(input("Nota da Avaliação 2 (Peso 4): "))
    n3 = float(input("Nota da Avaliação 3 (Peso 3): "))
    media = (n1 * 3 + n2 * 4 + n3 * 3) / 10
    estudantes.append({"nome": nome, "n1": n1, "n2": n2, "n3": n3, "media": media})
    
    if media > maior_media:
        maior_media = media
        melhor_estudante = nome
print("\n--- RELATÓRIO DE DESEMPENHO ---")
with open("notas.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome,Nota 1,Nota 2,Nota 3,Media\n")
    
    for est in estudantes:
        print(f"Estudante: {est['nome']} | Notas: {est['n1']}, {est['n2']}, {est['n3']} | Média: {est['media']:.2f}")
        arquivo.write(f"{est['nome']},{est['n1']},{est['n2']},{est['n3']},{est['media']:.2f}\n")
print(f"\n> Estudante com a maior média: {melhor_estudante} ({maior_media:.2f})")
print("> Os dados foram salvos com sucesso no arquivo 'notas.csv'.")

# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO