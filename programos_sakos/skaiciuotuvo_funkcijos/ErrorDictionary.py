class Errors:

    def __init__(self, **kwargs):
        self.errors = kwargs

    def get(self, key):
        return self.errors.get(key)

    def __getitem__(self, key): #galejau ir getattr, bet tiesiog pameginau su getitem
        return self.errors.get(key)

error_messages = Errors(
    e1="Klaida: įvestis negali būti tuščia",
    e2="Klaida: kvadratinė šaknis gali būti tik iš vieno skaičiaus",
    e3="Klaida: šaknis iš neigiamo skaičiaus",
    e4="Klaida: nežinomas veiksmas",
    e5="Klaida: neteisingi skaičiai",
    e6="Klaida: dalyba iš nulio",
    e7="Klaida: įveskite veiksmą formatu: skaičius operatorius skaičius",
    e8="Įvyko klaida:"
)
