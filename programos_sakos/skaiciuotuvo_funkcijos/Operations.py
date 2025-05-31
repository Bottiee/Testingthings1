from .ErrorDictionary import error_messages
from .Inputs_texts import ui_msg

class Operations:
    @staticmethod
    def is_valid_operator(op):
        return op in ui_msg.valid_operators

    @staticmethod
    def calculate(s1, op, s2):
        try:
            if op == ui_msg.root_operator:
                if s1 and not s2:
                    x = float(s1)
                elif s2 and not s1:
                    x = float(s2)
                else:
                    return error_messages["e2"]
                if x < 0:
                    return error_messages["e3"]
                return x ** 0.5
                #Maniau jog "//" buvo sqrt traukimas, x**.5 pakaitalas
            s1 = float(s1)
            s2 = float(s2)

            if op == "**":
                return s1 ** s2
            if op == "//":
                return s1 // s2
            if op == "+":
                return s1 + s2
            if op == "-":
                return s1 - s2
            if op == "*":
                return s1 * s2
            if op == "/":
                return s1 / s2
            return error_messages["e4"]
        except ValueError:
            return error_messages["e5"]
        except ZeroDivisionError:
            return error_messages["e6"]
