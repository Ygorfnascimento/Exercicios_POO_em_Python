from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.capacidade_carga = capacidade_carga

    def exibir_info(self):
        base_info = super().exibir_info()
        return f"{base_info}, Capacidade de carga: {self.capacidade_carga} toneladas"