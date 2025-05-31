def run_masinos():
    class Automobilis:
        def __init__(self, metai, modelis, kuro_tipas):
            self.metai = metai
            self.modelis = modelis
            self.kuro_tipas = kuro_tipas

        @staticmethod
        def vaziuoti():
            print("Važiuoja")

        @staticmethod
        def stoveti():
            print("Priparkuota")

        @staticmethod
        def pildyti_degalu():
            print("Degalai įpilti")


    class Elektromobilis(Automobilis):
        def pildyti_degalu(self):
            print("Baterija įkrauta")

        @staticmethod
        def vaziuoti_autonomiskai():
            print("Važiuoja autonomiškai")

#reikia perrasyti, kad leistu per pickle paciam irasyti masinas, metus ir kuro tipa
    automobiliai = [
        Automobilis(2018, "Toyota Corolla", "Benzinas"),
        Automobilis(2020, "Volkswagen Golf", "Dyzelinas"),
        Automobilis(2019, "Ford Focus", "Benzinas"),
        Elektromobilis(2023, "Tesla Model 3", "Elektra"),
        Elektromobilis(2024, "Nissan Leaf", "Elektra"),
        Elektromobilis(2022, "Hyundai Ioniq", "Elektra")
    ]

    print("Pasirinkite automobilį įvesdami jo numerį:")
    for indeksas, auto in enumerate(automobiliai):
        print(f"{indeksas + 1}. {auto.metai} {auto.modelis} ({auto.kuro_tipas})")

    pasirinkimas = int(input("Įveskite pasirinkimo numerį: ")) - 1
    pasirinktas_auto = automobiliai[pasirinkimas]

    print("\nPasirinkite veiksmą:")
    print("1. Važiuoti")
    print("2. Stovėti")
    print("3. Pildyti degalų / krauti bateriją")
    if isinstance(pasirinktas_auto, Elektromobilis):
        print("4. Važiuoti autonomiškai")

    veiksmas = int(input("Įveskite veiksmo numerį: "))

    print("\nRezultatas:")
    if veiksmas == 1:
        pasirinktas_auto.vaziuoti()
        print()
    elif veiksmas == 2:
        pasirinktas_auto.stoveti()
        print()
    elif veiksmas == 3:
        pasirinktas_auto.pildyti_degalu()
        print()
    elif veiksmas == 4 and isinstance(pasirinktas_auto, Elektromobilis):
        pasirinktas_auto.vaziuoti_autonomiskai()
        print()
    else:
        print("Neteisingas pasirinkimas.")