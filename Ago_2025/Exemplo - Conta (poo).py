class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo 

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Saldo não pode ser negativo!")

conta = ContaBancaria('Ygor Ferreira', 50000)

conta.depositar(100)
conta.sacar(100)

print(conta.ver_saldo())