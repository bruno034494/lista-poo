sair = "1"
while sair == "1":
    ultimo_digito = int(input("Informe o último dígito da placa do veículo: "))
    
    if ultimo_digito % 2 == 0:
        print(f"O número {ultimo_digito} é par.")
        print("O veículo deverá utilizar o Portão A.")
    else:
        print(f"O número {ultimo_digito} é ímpar.")
        print("O veículo deverá utilizar o Portão B.")
    sair = input("Deseja verificar outro veículo? (1 - Sim / 0 - Não): ")          
    print("====================================================================")
print("Programa finalizado com sucesso!")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO
