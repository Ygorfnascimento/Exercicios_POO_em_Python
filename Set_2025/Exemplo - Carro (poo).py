class Carro:
    def __init__(self, cor, modelo, marca, n_combustivel):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.n_combustivel = n_combustivel
        self.farol_ligado = False

    def andar(self):
        self.n_combustivel -= 2
        if self.n_combustivel <= 0:
            print("O nível de combustível acabou!")
            self.n_combustivel = 0
        elif self.n_combustivel <= 20:
            print("O nível de combustível está abaixo de 20:", self.n_combustivel)
        else:
            print("O carro andou! Nível atual de combustível:", self.n_combustivel)

    def buzinar(self):
        print("O carro está buzinando!")

    def ligar_farol(self):
        self.farol_ligado = True
        print("Farol ligado!")

    def desligar_farol(self):
        self.farol_ligado = False
        print("Farol desligado!")

    def menu(self):
        while True:
            print("\n--- MENU DO CARRO ---")
            print("1 - Andar")
            print("2 - Buzinar")
            print("3 - Ligar Farol")
            print("4 - Desligar Farol")
            print("5 - Sair")

            opcao = int(input("Digite uma opção: "))

            if opcao == 1:
                self.andar()
            elif opcao == 2:
                self.buzinar()
            elif opcao == 3:
                self.ligar_farol()
            elif opcao == 4:
                self.desligar_farol()
            elif opcao == 5:
                print("Você saiu do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

carro1 = Carro("Preto", "Honda Civic", "Honda", 100)

carro1.menu()