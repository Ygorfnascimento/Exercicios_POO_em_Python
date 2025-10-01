class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def apresentar(self):
        print(f"Nome: {self.nome}, idade: {self.idade}, profissão: {self.profissao}")

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
profissao = input("Digite a sua profissão atual: ")

pessoa1 = Pessoa(nome, idade, profissao)
pessoa1.apresentar()