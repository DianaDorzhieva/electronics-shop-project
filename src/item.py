import csv
word_csv = []


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message



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
        super().__init__() #для инициилизации класса Mixinlog
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'


    @classmethod
    def instantiate_from_csv(cls, file_way="../src/items.csv"):
        try:
            with open(file_way) as file:
                words = csv.DictReader(file)
                items = []
                for word in words:
                    if (word["name"] == None) or (word["price"] == None) or \
                            (word["quantity"] == None):
                        raise InstantiateCSVError
                    else:
                        name = word["name"]
                        price = float(word["price"])
                        quantity = int(word["quantity"])
                        item = cls(name, price, quantity)
                        items.append(item)
                    cls.all = items
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError:
            print("Файл item.csv поврежден")



    @staticmethod
    def string_to_number(some_string):
        string_number = some_string.split(".")
        return int(string_number[0])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

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

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise ValueError("складывать можно только классы Item")






