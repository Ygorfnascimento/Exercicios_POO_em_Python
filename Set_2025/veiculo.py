class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.ligado = False

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        if ano > 1885:
            self.__ano = ano
        else:
            raise ValueError("Ano inválido para um veículo.")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def exibir_info(self):
        status = "Ligado" if self.ligado else "Desligado"
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Ano: {self.__ano} - {status}"