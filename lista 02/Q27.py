def analisar_log(nome_arquivo):
    contagem = {}
    
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().lower()
            for caractere in conteudo:
                if caractere.isalpha():
                    if caractere in contagem:
                        contagem[caractere] += 1
                    else:
                        contagem[caractere] = 1
                        
        print("--- OCORRÊNCIAS NO ARQUIVO DE LOG ---")
        for letra, quantidade in sorted(contagem.items()):
            print(f"Letra '{letra}': {quantidade}")
            
    except FileNotFoundError:
        print("Arquivo de texto não encontrado. Crie o arquivo e tente novamente.")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO