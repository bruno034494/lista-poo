d = {}
sair = 1
def cadastrar_pokemon():
    while sair == 1:
        d["nome do pokemon"] = input("Qual é o nome do Pokémon: ")
        d["nivel"] = input("Qual é o nível do Pokémon: ")
def listar_pokemon():
    print("\nPokémon cadastrado com sucesso!")
    print(d)
def atualizar_pokemon():
    nome = input("Qual o nome do Pokémon que deseja atualizar? ")
    if nome in d:
        d[nome]["nivel"] = input("Qual é o novo nível do Pokémon? ")
        print("Pokémon atualizado com sucesso!")
    else:
        print("Pokémon não encontrado.")
def excluir_pokemon():
    nome = input("Qual o nome do Pokémon que deseja excluir? ")
    if nome in d:
        del d[nome]
        print("Pokémon excluído com sucesso!")
    else:
        print("Pokémon não encontrado.")
def pokemon_maior():
    if d:
        maior_nivel = max(d.values(), key=lambda x: x["nivel"])
        print(f"O Pokémon com o maior nível é: {maior_nivel['nome do pokemon']} com nível {maior_nivel['nivel']}.")
    else:
        print("Nenhum Pokémon cadastrado.")
def salvar_dadosjason():
    import json
    with open("pokemons.json", "w") as arquivo:
        json.dump(d, arquivo)
    print("Dados salvos em pokemons.json com sucesso!")
def carregar_dadosjason():
    import json
    try:
        with open("pokemons.json", "r") as arquivo:
            d = json.load(arquivo)
        print("Dados carregados de pokemons.json com sucesso!")
    except FileNotFoundError:
        print("Arquivo pokemons.json não encontrado.")
def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Pokémon")
        print("2. Listar Pokémon")
        print("3. Atualizar Pokémon")
        print("4. Excluir Pokémon")
        print("5. Mostrar Pokémon com maior nível")
        print("6. Salvar dados em JSON")
        print("7. Carregar dados de JSON")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_pokemon()
        elif opcao == "2":
            listar_pokemon()
        elif opcao == "3":
            atualizar_pokemon()
        elif opcao == "4":
            excluir_pokemon()
        elif opcao == "5":
            pokemon_maior()
        elif opcao == "6":
            salvar_dadosjason()
        elif opcao == "7":
            carregar_dadosjason()
        elif opcao == "8":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")





    main()