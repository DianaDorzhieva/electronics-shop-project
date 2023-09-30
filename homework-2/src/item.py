import csv
word_csv = []

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, file):
        with open("items.csv") as file:
            words = csv.DictReader(file)
            items = []
            print(words)
            for word in words:
                name = word["name"]
                price = float(word["price"])
                quantity = int(word["quantity"])
                item = cls(name, price, quantity)
                items.append(item)
            cls.all = items
        return cls.all

    @staticmethod
    def string_to_number(some_string):
        return int(some_string)

    @property
    def name(self):
        return self.__name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate



with open("items.csv") as file:
 words = csv.DictReader(file)
 items = []
 print(words)







