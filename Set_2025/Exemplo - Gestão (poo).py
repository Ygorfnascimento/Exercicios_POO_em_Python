class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.membros = []

    def adicionar_membro(self, funcionario):
        self.membros.append(funcionario)
        print(f"{funcionario.nome} foi adicionado ao projeto.")

    def remover_membro(self, nome):
        for membro in self.membros:
            if membro.nome.lower() == nome.lower():
                self.membros.remove(membro)
                print(f"{membro.nome} foi removido do projeto.")
                return
        print(f"Não foi encontrado nenhum membro com o nome '{nome}'.")

    def listar_membros(self):
        if not self.membros:
            print("Não há membros no projeto.")
        else:
            for membro in self.membros:
                print(f"Nome: {membro.nome}, Cargo: {membro.cargo}, Salário: R${membro.salario:.2f}")

    def custo_total(self):
        total = sum(m.salario for m in self.membros)
        print(f"O custo total do projeto é: R${total:.2f}")

def main():
   
    pessoa1 = Funcionario("Ygor", "CEO", 60000)
    pessoa2 = Funcionario("Pedro", "Chefe de Departamento", 60000)
    pessoa3 = Funcionario("Giovana", "Chefe de RH", 14000)
    pessoa4 = Funcionario("Sandra", "Desenvolvedora Web", 10000)
    pessoa5 = Funcionario("Cinthya", "Desenvolvedora Back-end", 10000)
    pessoa6 = Funcionario("Bruna", "Web Designer", 4000)
    
    projeto = Projeto("Sistema de RH", "Desenvolvimento de um sistema de RH")
    projeto.adicionar_membro(pessoa1)
    projeto.adicionar_membro(pessoa2)
    projeto.adicionar_membro(pessoa3)
    projeto.adicionar_membro(pessoa4)
    projeto.adicionar_membro(pessoa5)
    projeto.adicionar_membro(pessoa6)

    while True:
        print("\n------ MENU ------")
        print("1. Listar membros do projeto")
        print("2. Adicionar membro")
        print("3. Remover membro")
        print("4. Ver custo total do projeto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            projeto.listar_membros()

        elif opcao == "2":
            nome = input("Nome do novo membro: ")
            cargo = input("Cargo do novo membro: ")
            salario = float(input("Salário do novo membro: "))
            novo_membro = Funcionario(nome, cargo, salario)
            projeto.adicionar_membro(novo_membro)

        elif opcao == "3":
            nome = input("Digite o nome do membro a ser removido: ")
            projeto.remover_membro(nome)

        elif opcao == "4":
            projeto.custo_total()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

main()