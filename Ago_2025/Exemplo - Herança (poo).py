class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print("Au Au")

class Gato(Animal):
    def falar(self):
        print("Miau")

animais = {Animal("Genérico"), Cachorro("Rex"), Gato("Felix")}

for animal in animais:
    animal.falar()

#  c1 = Animal("Au")
#c1.falar()

#cachorro = Cachorro("Rex")
#cachorro.falar()

# gato = Gato("Miau")
# gato.falar()