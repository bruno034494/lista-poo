nome = input("Digite o nome: ")
data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

calculo_idade = 2026 - int(data_nascimento.split("/")[2])
print(f"{nome} tem {calculo_idade} anos.")
if calculo_idade < 18:
    print("Você é menor de idade e precisa de um acompanhante.")
else:
    print("Você é maior de idade e pode entrar sozinho.")
#CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO