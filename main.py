import requests
from abc import ABC, abstractmethod


def json_reader():
    url = 'https://drive.google.com/file/d/1fTgJX1_-rI2JbuM2He6OPyU_N5PyePsd/view'
    response = requests.get(url)
    data = response.json()
    return Category(name=data['name'],description=data['description'],products=data['products'])

class AbstractProduct(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def set_price(self, price):
        pass

    @abstractmethod
    def __str__(self):
        pass




class InfoMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join([f"{key} = {value}" for key, value in self.__dict__.items()])
        return f"{class_name}({attributes})"


class Products(InfoMixin, AbstractProduct):
    name: str
    description: str
    price: float
    quantity: int
    __count = 0

    @classmethod
    def __counter(cls):
        cls.__count += 1

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        print(repr(self))
        self.__counter()

    @classmethod
    def create_product(cls, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        return cls(name, description, price, quantity)


    @property
    def get_price(self):
        return self.price


    @price.setter
    def set_price(self,price):
        if price > 0:
            self.price = price
        else:
            print('Цена некорректна')

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт"


    def __add__(self, other):
        if type(self) == type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Должны быть одного класса")



class Category(InfoMixin):
    name: str
    description: str
    products: list
    __count = 0

    @classmethod
    def __counter(cls):
        cls.__count += 1

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        print(repr(self))
        self.__counter()


    def add_product(self,product):

        if not isinstance(product,Products):
            raise TypeError("Должны быть класса Продукты")
        self.__products.append(product)



    def __len__(self):
        return sum(self.quantity for product in self.__products)



    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)}"



    def avg_price(self):
        try:
           avg_price = sum(product.price for product in self.__products)/len(self.__products)
        except ZeroDivisionError:
            avg_price = 0
        return avg_price




class Smartphone(InfoMixin, Products):
    def __init__(self, name, description, price, quantity, performance, model, memory, colour):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.colour = colour
        print(repr(self))



class Grass(InfoMixin, Products):
    def __init__(self, name, description, price, quantity, country, term, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.term = term
        self.color = color
        print(repr(self))

