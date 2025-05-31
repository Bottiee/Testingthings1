import calendar
def run_leap():
    metai = int(input("Įveskite metus: "))
    if calendar.isleap(metai):
        print("Metai yra keliamieji\n")
    else:
        print("Metai yra nekeliamieji\n")
