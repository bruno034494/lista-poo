convidados = ["Natan", "Paulo", "Pablo", "Marcos", "João"]

print("--- CONVITES INICIAIS ---")
for pessoa in convidados:
    print(f"Olá {pessoa}, você está convidado para o jantar de hoje!")
desistente = "João"
print(f"\n--- ATUALIZAÇÃO ---")
print(f"Infelizmente, {desistente} não poderá comparecer.")

convidados[4] = "Lucas"

print("\n--- NOVOS CONVITES ---")
for pessoa in convidados:
    print(f"Olá {pessoa}, você está convidado para o jantar de hoje!")

# 3. Mesa maior: adicionando mais três convidados
print("\n--- MESA MAIOR: ADICIONANDO PESSOAS ---")
convidados.insert(0, "Ana")         
convidados.insert(3, "Carlos")      
convidados.append("Maria")        

print("\n--- CANCELAMENTOS ---")

while len(convidados) > 2:
    removido = convidados.pop()
    print(f"Sinto muito, {removido}, infelizmente não terei espaço na mesa.")
print("\n--- CONFIRMAÇÃO FINAL ---")
for pessoa in convidados:
    print(f"{pessoa}, seu convite ainda está confirmadíssimo!")
del convidados[0]
del convidados[0]

print("\nLista final após o jantar:", convidados)
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO