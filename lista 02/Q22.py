d = {
    "nome do estudante": "",
    "matricula": "",
    "curso": ""
}
def cadastrar_estudantes():
    """
    Função responsável por solicitar os dados do estudante pelo terminal.
    Ela percorre as chaves do dicionário e salva as respostas do usuário.
    """
    for chave in d.keys():
        d[chave] = input(f"Qual é o(a) {chave}: ")
def main():
    """
    Função principal que inicia o programa, executa o cadastro 
    e exibe o resultado final na tela.
    """
    cadastrar_estudantes()
    print("\nCadastrado com sucesso!")
    print(d) 
main()
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO