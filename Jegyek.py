class Targy:
    def __init__(self, nev, zh_szam, zh_aranyok, min_zh_eredmeny):
        self.nev = nev
        self.zh_szam = zh_szam
        self.zh_aranyok = zh_aranyok
        self.dolgozatok = []
        self.min_zh_eredmeny = min_zh_eredmeny

    def uj_dolgozat(self, pontszam):
        self.dolgozatok.append(pontszam)

    def erdemjegy(self):
        if not self.dolgozatok:
            return "Nincs eredmény"
        osszpontszam = sum(self.dolgozatok)
        osszarany = sum(self.zh_aranyok)
        erdemjegy = osszpontszam / osszarany if osszarany != 0 else 0
        if any(pontszam < 30 for pontszam in self.dolgozatok):
            return "Megtagadott aláírás"
        if erdemjegy < self.min_zh_eredmeny:
            return "Megtagadott aláírás"
        return self.kiszamitott_erdemjegy(erdemjegy)

    def kiszamitott_erdemjegy(self, erdemjegy):
        if erdemjegy <= 50:
            return 1
        elif erdemjegy <= 60:
            return 2
        elif erdemjegy <= 70:
            return 3
        elif erdemjegy <= 80:
            return 4
        else:
            return 5


class EgyetemiAlkalmazas:
    def __init__(self):
        self.targyak = []

    def uj_targy(self, nev, zh_szam, zh_aranyok, min_zh_eredmeny):
        targy = Targy(nev, zh_szam, zh_aranyok, min_zh_eredmeny)
        self.targyak.append(targy)

    def targy_kereses(self, nev):
        for targy in self.targyak:
            if targy.nev == nev:
                return targy
        return None


def uj_eredmenyek(alkalmazas):
    # Tantárgyak hozzáadása és eredmények bekérése
    for targy in alkalmazas.targyak:
        print(f"{targy.nev} eredmények megadása:")
        for i in range(targy.zh_szam):
            eredmeny = input(f"Zárthelyi {i+1}. eredmény: (átugrás - üres sor)")
            if eredmeny == "":
                break
            if eredmeny.isdigit():
                alkalmazas.targy_kereses(targy.nev).uj_dolgozat(int(eredmeny))
            else:
                alkalmazas.targy_kereses(targy.nev).uj_dolgozat(0)  # Ha nincs eredmény, az legyen 0
        print()


def eddigi_eredmenyek(alkalmazas):
    # Érdemjegyek kiszámítása és kiíratása
    print("Érdemjegyek:")
    for targy in alkalmazas.targyak:
        print(f"{targy.nev}: {targy.erdemjegy()}")


def main():
    alkalmazas = EgyetemiAlkalmazas()

    # Tantárgyak hozzáadása
    tantargyak = [
        ("Mesterséges Intelligencia", 4, [0.35, 0.35, 0.15, 0.15], 0.3),
        ("Nagyvállalati Linux (1. tantárgy)", 1, [1], 0.3),
        ("Nagyvállalati Linux (2. tantárgy)", 1, [1], 0.3),
        ("Architektúrák 2", 1, [1], 0.3),
        ("Rendszerfejlesztés", 5, [0.1, 0.1, 0.1, 0.1, 0.6], 0.3),
        ("Távközlési hálózatok", 2, [0.5, 0.5], 0.3)
    ]

    for nev, zh_szam, zh_aranyok, min_zh_eredmeny in tantargyak:
        alkalmazas.uj_targy(nev, zh_szam, zh_aranyok, min_zh_eredmeny)

    while True:
        valasztas = input("Kérem válasszon:\n1 - Új eredmények\n2 - Eddigi eredmények\n3 - Kilépés\n")
        if valasztas == "1":
            uj_eredmenyek(alkalmazas)
        elif valasztas == "2":
            eddigi_eredmenyek(alkalmazas)
        elif valasztas == "3":
            break
        else:
            print("Hibás választás, kérem válasszon újra!")


if __name__ == "__main__":
    main()
