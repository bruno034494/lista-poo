class cadastrar_equipamentos():
    def __init__(self):
        self.equipamentos = {}
    
    def cadastrar_equipamento(self):
        equipamento = input("Digite o nome do equipamento: ")
        self.equipamentos[equipamento] = True
        print(f"Equipamento '{equipamento}' cadastrado com sucesso!")
    def listar_equipamentos(self):
        if self.equipamentos:
            print("Equipamentos cadastrados:")
            for equipamento in self.equipamentos:
                print(f"- {equipamento}")
        else:
            print("Nenhum equipamento cadastrado.")
 
    def verificar_equipamento(self):
        equipamento = input("Digite o nome do equipamento que deseja verificar: ")
        if equipamento in self.equipamentos:
            print(f"Equipamento '{equipamento}' está cadastrado.")
        else:
            print(f"Equipamento '{equipamento}' não está cadastrado.")
    def arquivo_json(self):
        import json 
        with open ("equipamentos.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.equipamentos, arquivo)