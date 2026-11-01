import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


autot = []

for i in range(1, 11):
    tunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    auto = Auto(tunnus, huippunopeus)
    autot.append(auto)

kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_jatkuu = False

print(f"{'Rekisteri':<12}{'Huippunopeus':<16}{'Nopeus':<12}{'Matka':<12}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:<16}{auto.nopeus:<12}{auto.matka:<12.1f}")