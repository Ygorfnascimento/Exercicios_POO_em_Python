from random import randint
from datetime import datetime

import pytz

class ContaCorrente:
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('America/Sao_Paulo')
        data_hora_br = datetime.now(fuso_br)
        return data_hora_br.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, numero_conta):
        self.__saldo = 0
        self.__nome = nome
        self._cpf = cpf
        self.__limite = None
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f"Seu saldo é de: R$ {self.__saldo:.2f}")

    def depositar(self, valor):
        self.__saldo += valor
        self.transacoes.append(("Depósito", valor, self.__saldo, ContaCorrente._data_hora()))

    def limite_conta(self):
        self.__limite = -5000
        return self.__limite

    def saque(self, valor):
        if self.__limite is None:
            self.limite_conta()

        if self.__saldo - valor < self.__limite:
            print("Seu saldo é insuficiente!")
            self.consultar_saldo()
        else:
            self.__saldo -= valor
            print("Seu saque foi realizado com sucesso!")
            self.consultar_saldo()
            self.transacoes.append(("Saque", valor, self.__saldo, ContaCorrente._data_hora()))

    def consultar_transacoes(self):
        print("Histórico de Transações: ")
        for transacao in self.transacoes:
            print(transacao)

    def pedir_emprestimos(self, valor):
        sucess = self.agencia.emprestar_dinhero(valor, self._cpf, 0)

        if sucess:
            self.__saldo += valor
            self.transacoes.append(("Emprèstimo: ", valor, self.__saldo, ContaCorrente._data_hora()))

    def transferir(self, valor, conta_destino):
        if self.__saldo - valor < self.__limite:
            print("Saldo insuficiente!")
        else:
            self.__saldo -= valor
            self.transacoes.append(("Transferência enviada: ", valor, self.__saldo, ContaCorrente._data_hora()))
            conta_destino.__saldo += valor
            conta_destino.transacoes.append(("Transferência recebida: ", valor, conta_destino.__saldo, ContaCorrente._data_hora()))

class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('America/Sao_Paulo')
        data_hora_br = datetime.now(fuso_br)
        return data_hora_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(00000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = "{} / {} ".format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year)
        self.codigoseguranca = "{:03d}".format(randint(100, 999))
        self.limite = 5000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
        self._senha = 1234

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida!")

conta_pessoa = ContaCorrente("Maria", "111.111.111-2", "3333-2", "5555-8")
cartao_pessoa = CartaoCredito("maria", conta_pessoa)


print(cartao_pessoa. __dict__)

cartao_pessoa.senha = "1239"
print(cartao_pessoa.senha)


