class BaseParser:
    def __init__(self, input_str):
        self.grynas_input = input_str
        self.apkirptas_input = self.svarusis_input()

    def svarusis_input(self):
        return self.grynas_input.replace(" ", "")

class InputParser(BaseParser):
    def __init__(self, input_str):
        super().__init__(input_str)
        self.start = 1 if self.apkirptas_input and self.apkirptas_input[0] in "+-" else 0

    def parse(self):
        s = self.apkirptas_input
        start = self.start
        for i in range(start, len(s) - 1):
            if s[i:i+2] == "**":
                return s[:i], "**", s[i+2:]
            if s[i:i+2] == "//":
                return s[:i], "//", s[i+2:]
        for i, ch in enumerate(s[start:], start):
            if ch in "+-*/v":
                return s[:i], ch, s[i+1:]
        return None, None, None

# Paimama įvestis ir išvalomi tarpai
# Patikrinama, ar pradžioje yra + arba -
# Tikrinami dvigubi operatoriai (pvz., "**", "//"), tada viengubi
# Jei dvigubi operatoriai nerandami, atliekamas ciklas per simbolius su indeksais "i" ir "ch"
# Jei "ch" yra viengubas operatorius iš nurodyto sąrašo, atliekamas skaidymas
# Jei operatorių nėra, grąžinama tuple su trimis None reikšmėmis