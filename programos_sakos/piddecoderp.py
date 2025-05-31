def pid_info():
    pid = input("Įveskite savo asmens kodą: ")
    if len(pid) == 11 and pid.isdigit():
        pid_tuple = tuple(pid)
        a, b, c, d, e, f, g, h, i, j, k = [int(d) for d in pid_tuple]

        if a != 9:
            x = a*1 + b*2 + c*3 + d*4 + e*5 + f*6 + g*7 + h*8 + i*9 + j*1
            y = x % 11
            if y != 10:
                is_valid_check = (y == k)
            else:
                x = a*3 + b*4 + c*5 + d*6 + e*7 + f*8 + g*9 + h*1 + i*2 + j*3
                y = x % 11
                is_valid_check = (k == 0) if y == 10 else (y == k)
            if not is_valid_check:
                print("Asmens kodas neteisingas")
                return None
        else:
            is_valid_check = True

        gender_key = {
            1: ("Vyras", 1800),
            2: ("Moteris", 1800),
            3: ("Vyras", 1900),
            4: ("Moteris", 1900),
            5: ("Vyras", 2000),
            6: ("Moteris", 2000),
            9: ("Nenustatyta", None),
        }

        gender, century = gender_key.get(a, ("Invalid", None))
        if century is None:
            birth_year = birth_month = birth_day = "Nenustatyta"
        else:
            year = int(f"{b}{c}")
            month = int(f"{d}{e}")
            day = int(f"{f}{g}")

            #Nezinau ar puikiai pavyko itraukti isimtis asmens kodo, tas retas
            birth_month = "Nenustatytas gimimo mėnuo" if month == 0 else month
            birth_day = "Nenustatyta gimimo diena" if day == 0 else day
            birth_year = century + year

        birthdate_key = {
            "year": birth_year,
            "month": birth_month,
            "day": birth_day,
            "gender": gender
        }

        return {
            "pid_tuple": pid_tuple,
            "digits": [a, b, c, d, e, f, g, h, i, j, k],
            "birth_info": birthdate_key,
            "valid": is_valid_check
        }
    else:
        print("Neteisingai įvestas asmens kodas")
        return None


def pd_info():
    pid_data = pid_info()
    if pid_data:
        birth = pid_data["birth_info"]
        print(f"Lytis: {birth['gender']}")
        print(f"Metai: {birth['year']}")
        print(f"Mėnuo: {birth['month']}")
        print(f"Diena: {birth['day']}\n")