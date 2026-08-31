def filtrar_tempos_resposta(tempos, limite_inferior, limite_superior):
    """
    Recebe uma lista de tempos de resposta e exibe uma sublista
    apenas com os valores dentro do limite estabelecido.
    """
    sublista = []
    for tempo in tempos:
        
        if limite_inferior <= tempo <= limite_superior:
    
            sublista.append(tempo)
            
    print(f"Sublista gerada: {sublista}")
tempos_registrados = [12, 25, 33, 45, 52, 68, 75, 89, 102]

print("Tempos originais do servidor:", tempos_registrados)
print("Buscando requisições entre 30ms e 75ms...")

filtrar_tempos_resposta(tempos_registrados, 30, 75)
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO