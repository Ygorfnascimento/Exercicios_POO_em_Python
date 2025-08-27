class Pessoa :
    def __init__(self, nome):
        self.nome = nome

    def dizer_oi(self):
        print(f"Oi, meu nome é: {self.nome}")

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")
pessoa1.dizer_oi()
pessoa2.dizer_oi()