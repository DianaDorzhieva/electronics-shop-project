from src.item import Item
class Mixinlog:
    def __init__(self):
        language = "EN"
        self.language = language


    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"

    def save_language(self):
        print(f"Настроен язык клавиатуры - {self.language} ")



class Keyboard(Item,Mixinlog):
    def __init__(self, name: str, price: float, quantity: int,language="EN"):
        super().__init__(name, price, quantity)
        self.language = language
        if self.language.upper() != "EN" and self.language.upper() != "RU":
            raise ValueError("Язык клавиатуры может быть только EN или RU")



