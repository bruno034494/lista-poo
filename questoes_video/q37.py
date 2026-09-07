import json 

class gerenciarPokemon:
    def __init__(self):
        self.d = {}
    
    def cadastrar_pokemon(self):
        nome = input("Qual o nome do Pokémon? ")
        # Convertido para int() para cálculos futuros
        nivel = int(input("Qual o nível do Pokémon? "))
        self.d[nome] = {"nome do pokemon": nome, "nivel": nivel}
        print("Pokémon cadastrado com sucesso!")
    
    def listar_pokemon(self):
        if self.d:
            for nome, info in self.d.items():
                print(f"Nome: {info['nome do pokemon']}, Nível: {info['nivel']}")
        else:
            print("Nenhum Pokémon cadastrado.")
            
    def atualizar_pokemon(self):
        nome = input("Qual o nome do Pokémon que deseja atualizar? ")
        if nome in self.d:
            # Convertido para int() aqui também
            self.d[nome]["nivel"] = int(input("Qual é o novo nível do Pokémon? "))
            print("Pokémon atualizado com sucesso!")
        else:
            print("Pokémon não encontrado.")
            
    def excluir_pokemon(self):
        nome = input("Qual o nome do Pokémon que deseja excluir? ")
        if nome in self.d:
            del self.d[nome]
            print("Pokémon excluído com sucesso!")
        else:
            print("Pokémon não encontrado.")
            
    def pokemon_maior(self):
        if self.d:
            maior_nivel = max(self.d.values(), key=lambda x: x["nivel"])
            print(f"O Pokémon com o maior nível é: {maior_nivel['nome do pokemon']} com nível {maior_nivel['nivel']}.")
        else:
            print("Nenhum Pokémon cadastrado.")
            
    def salvar_dadosjason(self):
        with open("pokemons.json", "w") as arquivo:
            json.dump(self.d, arquivo)
        print("Dados salvos em pokemons.json com sucesso!")
        
    def carregar_dadosjason(self):
        try:
            with open("pokemons.json", "r") as arquivo:
                self.d = json.load(arquivo)
            print("Dados carregados de pokemons.json com sucesso!")
        except FileNotFoundError:
            print("Arquivo pokemons.json não encontrado.")

def main():
    # As boas-vindas e a criação do objeto vêm ANTES do loop infinito
    print("Bem-vindo ao Gerenciador de Pokémon!\n")
    gerenciador = gerenciarPokemon()
    gerenciador.carregar_dadosjason()

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
            gerenciador.cadastrar_pokemon()
        elif opcao == "2":
            gerenciador.listar_pokemon()
        elif opcao == "3":
            gerenciador.atualizar_pokemon()
        elif opcao == "4":
            gerenciador.excluir_pokemon()
        elif opcao == "5":
            gerenciador.pokemon_maior()
        elif opcao == "6":
            gerenciador.salvar_dadosjason()
        elif opcao == "7":
            gerenciador.carregar_dadosjason()
        elif opcao == "8":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()