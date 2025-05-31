class Atsakymai:

    def __init__(self, **kwargs):
        self.atsakymai = kwargs

    def __getattr__(self, name): #Realiai vien del "." iskvietimo panaudojau sita
        if name in self.atsakymai:
            return self.atsakymai[name]
        raise AttributeError(f"'{self.__class__.__name__}' Objektas neturi rakto pavadinimu '{name}'")

#Galima pildyti jei noriu papildomu funkciju prideti
ui_msg = Atsakymai(
    exit_info="Norėdami nutraukti programą, įveskite: stop\n",
    userprompt="Įveskite skaičių veiksmą (pvz. 10 * -1): \n",
    exit_input="stop",
    exit_success="Programa nutraukta.",
    result_s="Rezultatas:",
    true_str="Tiesa",
    false_str="Netiesa",
    zero_info="Daugiau nei nulis:",
    valid_operators="+-*/**//v",
    root_operator="v"
)