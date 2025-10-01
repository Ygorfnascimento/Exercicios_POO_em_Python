from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    def exibir_info(self):
        base_info = super().exibir_info()
        return f"{base_info}, Portas: {self.num_portas}"