class Pato:
    def voar(self):
        print("Pato voando...")

class Aviao:
    def voar(self):
        print("Voando . . . ")


def fazer_voar(objeto):
    objeto.voar()

patolino = Pato()
aviao = Aviao()

fazer_voar(patolino)
fazer_voar(aviao)