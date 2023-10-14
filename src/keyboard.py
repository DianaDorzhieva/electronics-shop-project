from src.item import Item


class Mixinlog:
    def __init__(self):
        language = "EN"
        self.__language = "EN"
        if self.__language.upper() != "EN" and self.language.upper() != "RU":
            raise AttributeError("Язык клавиатуры может быть только EN или RU")
        self.__language = language

    @property
    def language(self):
        return self.__language

    # @language.setter
    # def language(self, language):
    #     if language.upper() != "EN" and language.upper() != "RU":
    #         raise AttributeError("Язык клавиатуры может быть только EN или RU")
    #     self.__language = language.upper()

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    def save_language(self):
        print(f"Настроен язык клавиатуры - {self.__language} ")


class Keyboard(Item, Mixinlog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        Mixinlog.__init__(self)
