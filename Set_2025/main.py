from carro import Carro
from moto import Moto
from caminhao import Caminhao

def mostrar_menu(carro_list, moto_list, caminhao_list):
    print("\nMenu:")

    algum_ligado = any(veiculo.ligar for veiculo in carro_list + moto_list + caminhao_list)

    print("1 - Adicionar Carro")
    print("2 - Adicionar Moto")
    print("3 - Adicionar Caminhão")

    if algum_ligado:
        print("4 - Desligar todos os veículos")
    else:
        print("4 - Ligar todos os veículos")

    print("5 - Ver informações da frota")
    print("6 - Sair")

def adicionar_carro():
    print("\n--- Adicionando Carro ---")
    marca = input("Marca do carro: ")
    modelo = input("Modelo do carro: ")
    ano = int(input("Ano do carro: "))
    portas = int(input("Número de portas: "))
    return Carro(marca, modelo, ano, portas)

def adicionar_moto():
    print("\n--- Adicionando Moto ---")
    marca = input("Marca da moto: ")
    modelo = input("Modelo da moto: ")
    ano = int(input("Ano da moto: "))
    cilindradas = int(input("Cilindradas da moto: "))
    return Moto(marca, modelo, ano, cilindradas)

def adicionar_caminhao():
    print("\n--- Adicionando Caminhão ---")
    marca = input("Marca do caminhão: ")
    modelo = input("Modelo do caminhão: ")
    ano = int(input("Ano do caminhão: "))
    carga = float(input("Capacidade de carga (em toneladas): "))
    return Caminhao(marca, modelo, ano, carga)

def main():
    carro_list = []
    moto_list = []
    caminhao_list = []

    while True:
        mostrar_menu(carro_list, moto_list, caminhao_list)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carro = adicionar_carro()
            carro_list.append(carro)
            print("Carro adicionado com sucesso!")

        elif opcao == "2":
            moto = adicionar_moto()
            moto_list.append(moto)
            print("Moto adicionada com sucesso!")

        elif opcao == "3":
            caminhao = adicionar_caminhao()
            caminhao_list.append(caminhao)
            print("Caminhão adicionado com sucesso!")

        elif opcao == "4":
            if not carro_list and not moto_list and not caminhao_list:
                print("A frota está vazia. Adicione algum veículo primeiro.")
            else:
                algum_ligado = any(veiculo.ligar for veiculo in carro_list + moto_list + caminhao_list)

                if algum_ligado:
                    for veiculo in carro_list + moto_list + caminhao_list:
                        veiculo.desligar()
                    print("Todos os veículos foram desligados!")
                else:
                    for veiculo in carro_list + moto_list + caminhao_list:
                        veiculo.ligar()
                    print("Todos os veículos foram ligados!")

        elif opcao == "5":
            if not carro_list and not moto_list and not caminhao_list:
                print("A frota está vazia. Adicione algum veículo primeiro.")
            else:
                print("\n--- Informações da Frota ---")
                for veiculo in carro_list + moto_list + caminhao_list:
                    print(veiculo.exibir_info())

        elif opcao == "6":
            print("Saindo do programa")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()