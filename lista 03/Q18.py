nomes = []
precos = []
for i in range(5):
    nome = input(f"Nome do {i+1}º equipamento: ")
    preco = float(input(f"Preço do {i+1}º equipamento: R$ "))
    nomes.append(nome)
    precos.append(preco)
maior_preco = max(precos)
indice_maior = precos.index(maior_preco)

equipamento_caro = nomes[indice_maior]

print(f"\nO equipamento mais caro é o(a) '{equipamento_caro}' custando R$ {maior_preco:.2f}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO