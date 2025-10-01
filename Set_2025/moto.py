from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_info(self):
        base_info = super().exibir_info()
        return f"{base_info}, Cilindradas: {self.cilindradas}cc"