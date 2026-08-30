def exibir_nome_do_programa():
    """
    Exibe o nome do programa de forma destacada.
    Não recebe parâmetros e não retorna valores.
    """
    print("=========================================")
    print("   Sistema de Gerenciamento Acadêmico")
    print("=========================================")

def exibir_menu():
    """
    Exibe o menu de opções do sistema para o usuário.
    Não recebe parâmetros e não retorna valores.
    """
    print("\n-------- SISTEMA ACADÊMICO --------")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Alterar situação")
    print("0 - Sair")

def cadastrar_estudante():
    """
    Simula a etapa de cadastro de um estudante.
    Não recebe parâmetros e não retorna valores.
    """
    print("-> Opção Cadastrar estudante selecionada.")

def listar_estudantes():
    """
    Simula a etapa de listagem dos estudantes.
    Não recebe parâmetros e não retorna valores.
    """
    print("-> Opção Listar estudantes selecionada.")

def alterar_situacao_estudante():
    """
    Simula a etapa de alteração da situação de um estudante.
    Não recebe parâmetros e não retorna valores.
    """
    print("-> Opção Alterar situação selecionada.")

def opcao_invalida():
    """
    Informa que a opção escolhida pelo usuário não existe.
    Não recebe parâmetros e não retorna valores.
    """
    print("-> Opção inválida! Por favor, tente novamente.")

def finalizar_programa():
    """
    Informa ao usuário que o sistema está sendo encerrado.
    Não recebe parâmetros e não retorna valores.
    """
    print("-> O sistema está sendo encerrado. Até logo!")

def main():
    """
    Função principal que coordena a execução do programa.
    Apresenta o nome do sistema, o menu e processa a escolha do usuário em um loop.
    """
    exibir_nome_do_programa()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_estudante()
        elif opcao == '2':
            listar_estudantes()
        elif opcao == '3':
            alterar_situacao_estudante()
        elif opcao == '0':
            finalizar_programa()
            break  
        else:
            opcao_invalida()
if __name__ == "__main__":
    main()
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO