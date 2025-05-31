from programos_sakos.darbuotojaip import run_darbas
from programos_sakos.piddecoderp import pd_info
from programos_sakos.automobiliaip import run_masinos
from programos_sakos.leapyearp import run_leap
from programos_sakos.currenttimep import run_laikodelta
from programos_sakos.skaiciuotuvasp import run_skaiciuotuvas

def pasirinkimai():
    print("\nPasirinkite norimą programą:")
    print("1 - Skaiciuotuvas")
    print("2 - Asmens kodo patikrinimas")
    print("3 - Keliamieji metai")
    print("4 - Praėjęs laikas nuo datos")
    print("5 - Automobiliai")
    print("6 - Darbuotojas")
    print("help - Priminti galimus pasirinkimus")
    print("q - Nutraukti programų pasirinkimą.")

#Viska galima dar perskirti per atskirus .py failus, bet pagrindinis failas liks tuscias ir man tas negrazu

def main():
    pasirinkimai()
    while True:
        pasirinkimas = input("Jūsų pasirinkimas: ").strip().lower()

        if pasirinkimas == "1":
            run_skaiciuotuvas()
        elif pasirinkimas == "2":
            print()
            pd_info()
        elif pasirinkimas == "3":
            print()
            run_leap()
        elif pasirinkimas == "4":
            print()
            run_laikodelta()
        elif pasirinkimas == "5":
            print()
            run_masinos()
        elif pasirinkimas == "6":
            print()
            run_darbas()
        elif pasirinkimas == "help":
            print()
            pasirinkimai()
        elif pasirinkimas == "q":
            print("Programa nutraukta.")
            print()
            break
        else:
            print("Neteisingas pasirinkimas")

            