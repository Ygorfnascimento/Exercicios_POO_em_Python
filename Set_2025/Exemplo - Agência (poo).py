from random import randint
from banco import ContaCorrente

class Agencia:
    def __init__(self, numero, telefone, cnpj):
        self.numero = numero
        self.telefone = telefone
        self.cnpj = cnpj
        self.clientes = []
        self.caixa = 10000
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 2000000:
            print(f"Caixa abaixo do nível recomendado! caixa atual: {self.caixa}")
        else:
            print(f"O nível do caixa está ok, caixa atual: {self.caixa}")

    def emprestar_dinhero(self, valor, cpf, juros):
        if self.caixa > valor:
            print("O empréstimo foi realizado com sucesso!")
            self.caixa -= valor
            self.emprestimos.append((valor, cpf, juros))
            return True
        else:
            print("Não foi possível realizar o empréstimo.")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):
    def __init__(self,site, numero, telefone, cnpj):
        self.site = site
        super().__init__(numero,telefone,cnpj)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor


class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(randint(1001, 9999), telefone, cnpj)
        self.caixa = 1000000

class Agencia_premium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(randint(1001, 9999), telefone, cnpj)
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("Cliente não possui o patrimônio mínimo necessário")


agencia1 = Agencia("4444", "59590-4558","12.345.678/0001-00" )
agencia_comum = Agencia("4444", "59590-4558","12.345.678/0001-00" )
agencia_premium = Agencia("4444", "59590-4558","12.345.678/0001-00" )
agencia_virtual = Agencia("4444", "59590-4558","12.345.678/0001-00" )


agencia_virtual = AgenciaVirtual("www.agencia.com","1456", "40028922","00.000.000/0001-00")
# print(agencia_virtual.__dict__)
# print("-------------------------------------------------------------------------------------------------------------------\n")

agencia_comum = AgenciaComum(4454489, 12345678901234)
agencia_comum.verificar_caixa()
# print(agencia_comum.__dict__)
# print("-------------------------------------------------------------------------------------------------------------------\n")

agencia_comum = AgenciaComum(44448489, 10987654321123)
agencia_comum.verificar_caixa()
# print(agencia_comum.__dict__)
# print("-------------------------------------------------------------------------------------------------------------------")

# agencia_virtual.depositar_paypal(25000)
# print(f"Caixa virtual: R$ {agencia_virtual.caixa}")
# print(f"Caixa paypal: R$ {agencia_virtual.caixa_paypal}")
if __name__ == '__main__':

    agencia1.adicionar_cliente("José", 12345678900, 1000000)
    print("Clietes agencia1:", agencia1.clientes)

    agencia_comum.adicionar_cliente("José", 12345678900, 1000000)
    print("Clietes agencia comum:", agencia_comum.clientes)

    agencia_virtual.adicionar_cliente("José", 12345678900, 1000000)
    print("Clietes agencia comum:", agencia_virtual.clientes)

    agencia_premium.adicionar_cliente("José", 12345678900, 1000000)
    print("Clietes agencia pemium:", agencia_premium.clientes)