import datetime


def run_laikodelta():
    now = datetime.datetime.today()
    while True:
        print("Įveskite datą")

        metai_input = input("Metai: ")
        metai = int(metai_input) if metai_input else 1  # 1 AD is earliest supported year

        menuo_input = input("Mėnuo: ")
        menuo = int(menuo_input) if menuo_input else 1

        diena_input = input("Diena: ")
        diena = int(diena_input) if diena_input else 1

        try:
            data = datetime.datetime(
                year=metai,
                month=menuo,
                day=diena,
            )
            break
        except ValueError as err:
            print("Neteisingai įvesta data:", err)

    delta = now - data

    print(f"Nuo {data} datos praėjo:")
    print("Metų:", round(delta.days // 365.25))
    print("Mėnesių:", round(delta.days // 365.25 * 12))
    print("Savaičių:", round(delta.days // 7))
    print("Dienų:", delta.days)
    print("Valandų:", round(delta.total_seconds() // 3600))
    print("Minučių:", round(delta.total_seconds() // 60))
    print("Sekundžių:", round(delta.total_seconds()), "\n")
#Aciu destytojui uz koda, pasiskolinu ji sau su mini pakeitimais

