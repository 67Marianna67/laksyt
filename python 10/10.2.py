class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)


class Talo:
    def __init__(self, alin, ylin, hissit):
        self.hissit = []
        for i in range(hissit):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi, kohde):
        self.hissit[hissi].siirry_kerrokseen(kohde)


talo = Talo(1, 10, 3)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.aja_hissiä(2, 3)