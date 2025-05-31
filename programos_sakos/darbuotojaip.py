from datetime import datetime, timedelta
def run_darbas():
    class Darbuotojas:
        def __init__(self, input_vardas, input_pavarde, valandos_ikainis, dirba_nuo):
            self.vardas = input_vardas
            self.pavarde = input_pavarde
            self.valandos_ikainis = valandos_ikainis
            self.dirba_nuo = datetime.strptime(dirba_nuo, "%Y-%m-%d")
            self.last_paid = self.dirba_nuo

        def skaiciuoti_darbo_dienas(self):
            siandien = datetime.today()
            skirtumas = siandien - self.last_paid
            return skirtumas.days

        def skaiciuoti_visas_darbo_dienas_nuo_pradzios(self):
            siandien = datetime.today()
            visos_dienos = (siandien - self.dirba_nuo).days
            darbo_dienos = (visos_dienos // 7) * 5 + min(5, visos_dienos % 7)
            return darbo_dienos

        def paskaiciuoti_atlyginima(self):
            darbo_dienos = self.skaiciuoti_darbo_dienas()
            valandos = darbo_dienos * 8
            return valandos * self.valandos_ikainis

        def paskaiciuoti_bendra_atlyginima(self):
            alga_dienos = self.skaiciuoti_visas_darbo_dienas_nuo_pradzios()
            valandos = alga_dienos * 8
            return valandos * self.valandos_ikainis

        def trumpa_info(self):
            return f"{self.vardas} {self.pavarde}, dirba nuo {self.dirba_nuo.date()}"

        def likusios_dienos_iki_kitos_ismokos(self):
            siandien = datetime.today()
            kitas_mokejimas = self.last_paid + timedelta(days=30)
            return max(0, (kitas_mokejimas - siandien).days)

        def ismokejimas(self):
            atlyginimas = self.paskaiciuoti_atlyginima()
            self.last_paid = datetime.today()
            return atlyginimas

    visi_darbuotojai = []
    bazinis_ikainis = 11.0
#dar reikes naujos klases su "esami darbuotojai", bet kol kas uztenka ir taip
    visi_darbuotojai.append(Darbuotojas("Manfredas", "Šiaulys", bazinis_ikainis + 2, "2024-01-01"))
    visi_darbuotojai.append(Darbuotojas("Nonatas", "Doreika", bazinis_ikainis, "2024-01-15"))

    while True:
        print("\nPasirinkite veiksmą:")
        print("1 - Pridėti naują darbuotoją")
        print("2 - Peržiūrėti visus darbuotojus")
        print("3 - Patikrinti atlyginimus")
        print("4 - Atlikti išmokėjimą (Pay Day)")
        print("5 - Išeiti")
        print("6 - Patikrinti darbuotojo darbo dienas ir bendrą uždarbį")
        pasirinkimas = input("Įveskite pasirinkimą: ")

        if pasirinkimas == "1":
            vardas = input("Įveskite vardą: ")
            pavarde = input("Įveskite pavardę: ")
            data_str = input("Įveskite darbo pradžios datą (YYYY-MM-DD): ")
            try:
                naujas_darbuotojas = Darbuotojas(vardas, pavarde, bazinis_ikainis, data_str)
                visi_darbuotojai.append(naujas_darbuotojas)
                print(f"Sėkmingai pridėtas darbuotojas: {naujas_darbuotojas.trumpa_info()}")
            except ValueError:
                print("Neteisingas datos formatas. Naudokite YYYY-MM-DD.")

        elif pasirinkimas == "2":
            if not visi_darbuotojai:
                print("Darbuotojų sąrašas tuščias.")
            else:
                for d in visi_darbuotojai:
                    print(d.trumpa_info())

        elif pasirinkimas == "3":
            print("\nAtlyginimų patikrinimas:")
            for d in visi_darbuotojai:
                print(f"{d.vardas} {d.pavarde} - Atlyginimas: {d.paskaiciuoti_atlyginima():.2f} EUR, "
                      f"Dienų iki kitos išmokos: {d.likusios_dienos_iki_kitos_ismokos()}")

        elif pasirinkimas == "4":
            print("\nIšmokėjimų vykdymas:")
            for d in visi_darbuotojai:
                ismoketa = d.ismokejimas()
                print(f"{d.vardas} {d.pavarde} buvo išmokėta: {ismoketa:.2f} EUR.")

        elif pasirinkimas == "5":
            print("Programa baigta.")
            break

        elif pasirinkimas == "6":
            if not visi_darbuotojai:
                print("Darbuotojų sąrašas tuščias.")
                continue
            print("\nPasirinkite darbuotoją:")
            for i, d in enumerate(visi_darbuotojai, 1):
                print(f"{i}: {d.vardas} {d.pavarde}")
            try:
                pasirinktas = int(input("Įveskite numerį: ")) - 1
                if 0 <= pasirinktas < len(visi_darbuotojai):
                    darbuotojas = visi_darbuotojai[pasirinktas]
                    dienos = darbuotojas.skaiciuoti_visas_darbo_dienas_nuo_pradzios()
                    suma = darbuotojas.paskaiciuoti_bendra_atlyginima()
                    print(f"{darbuotojas.vardas} {darbuotojas.pavarde} dirba {dienos} darbo dienas ir uždirbo {suma:.2f} EUR nuo įdarbinimo.")
                else:
                    print("Neteisingas pasirinkimas.")
            except ValueError:
                print("Blogas įvesties formatas.")

        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
