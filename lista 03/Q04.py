softwares = ["Windows", "Pacote Office", "Google Chrome", "Antivírus", "Leitor de PDF"]

print("--- LISTA ORIGINAL ---")
print(softwares)
print()

novo_software = input("Digite o nome do novo software a ser instalado: ")
softwares.append(novo_software)

softwares.pop(1)

print("\n--- LISTA ATUALIZADA ---")
print(softwares)
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO