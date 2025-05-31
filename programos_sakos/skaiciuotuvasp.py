from .skaiciuotuvo_funkcijos.ErrorDictionary import error_messages
from .skaiciuotuvo_funkcijos.InputParser import InputParser
from .skaiciuotuvo_funkcijos.Operations import Operations
from .skaiciuotuvo_funkcijos.NumberFormatter import NumberFormatter
from .skaiciuotuvo_funkcijos.Inputs_texts import ui_msg
#noretusi kazkaip vieno didelio importo kaip bibliotekos su manom funkcijom
def run_skaiciuotuvas():
    print(ui_msg.exit_info)

    while True:
        result = None
        try:
            uinpt = input(ui_msg.userprompt).strip()
            if not uinpt:
                print(error_messages["e1"] + "\n")
                continue
            if uinpt.lower() == ui_msg.exit_input:
                print(ui_msg.exit_success)
                print()
                break
            s1, op, s2 = InputParser(uinpt).parse()
            if None in (s1, op, s2) or not Operations.is_valid_operator(op):
                print(error_messages["e7"] + "\n")
                continue
            result = Operations.calculate(s1, op, s2)
        except Exception as e:
            print(error_messages["e8"], e)
        else:
            print(ui_msg.result_s, NumberFormatter.nuliui_ne(result))
        finally:
            if isinstance(result, (int, float)):
                boollt = {True: ui_msg.true_str, False: ui_msg.false_str}
                print(ui_msg.zero_info, boollt[result > 0])
            #kita kart gal nerasyti kintamuju kaip vienos raides