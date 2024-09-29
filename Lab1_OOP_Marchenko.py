from abc import ABC, abstractmethod
from typing import List

# <----- Базові класи ----->

class User(ABC):  # Абстрактний клас (Інкапсуляція, Наслідування)
    def __init__(self, username: str, email: str):
        self.__username = username
        self.__email = email
    
    @abstractmethod
    def get_user_type(self):
        pass

    def get_email(self):  # Нетривіальний метод (Інкапсуляція)
        return self.__email

    def set_email(self, email: str):  # Нетривіальний метод (Інкапсуляція)
        self.__email = email


class Product(ABC):  # Абстрактний клас (Інкапсуляція, Наслідування)
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @abstractmethod
    def get_category(self):
        pass

    def get_price(self):  # Нетривіальний метод
        return self._price

    def apply_discount(self, discount: float):  # Нетривіальний метод (Поліморфізм)
        self._price -= self._price * discount

# <----- Ієрархія наслідування 1 (Класи користувачів) ----->

class Customer(User):  # Наслідує від User
    def __init__(self, username: str, email: str):
        super().__init__(username, email)
        self.cart: List[Product] = []

    def add_to_cart(self, product: Product):  # Нетривіальний метод
        self.cart.append(product)

    def get_total_cart_value(self):  # Нетривіальний метод
        return sum(item.get_price() for item in self.cart)

    def get_user_type(self):  # Реалізація абстрактного методу
        return "Customer"


class Vendor(User):  # Наслідує від User
    def __init__(self, username: str, email: str, store_name: str):
        super().__init__(username, email)
        self.__store_name = store_name
        self.products: List[Product] = []

    def add_product(self, product: Product):  # Нетривіальний метод
        self.products.append(product)

    def list_products(self):  # Нетривіальний метод
        return [product._name for product in self.products]

    def get_user_type(self):  # Реалізація абстрактного методу
        return "Vendor"


class Admin(User):  # Наслідує від User
    def __init__(self, username: str, email: str):
        super().__init__(username, email)

    def ban_user(self, user: User):  # Нетривіальний метод
        print(f"User {user.get_email()} заблокований.")

    def get_user_type(self):  # Реалізація абстрактного методу
        return "Admin"

# <----- Ієрархія наслідування 2 (Класи продуктів) ----->

class Electronic(Product):  # Наслідує від Product
    def __init__(self, name: str, price: float, warranty: int):
        super().__init__(name, price)
        self.__warranty = warranty

    def extend_warranty(self, years: int):  # Нетривіальний метод
        self.__warranty += years

    def get_category(self):  # Реалізація абстрактного методу
        return "Electronic"


class Clothing(Product):  # Наслідує від Product
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.__size = size

    def change_size(self, new_size: str):  # Нетривіальний метод
        self.__size = new_size

    def get_category(self):  # Реалізація абстрактного методу
        return "Clothing"


class Furniture(Product):  # Наслідує від Product
    def __init__(self, name: str, price: float, material: str):
        super().__init__(name, price)
        self.__material = material

    def set_material(self, new_material: str):  # Нетривіальний метод
        self.__material = new_material

    def get_category(self):  # Реалізація абстрактного методу
        return "Furniture"

# <----- Поліморфізм (Статичний і Динамічний) ----->

class DiscountManager:
    def apply_bulk_discount(self, products: List[Product], discount: float):  # Статичний поліморфізм (Перевантаження методу)
        for product in products:
            product.apply_discount(discount)

    def apply_targeted_discount(self, product: Product, discount: float):  # Інший приклад статичного поліморфізму
        product.apply_discount(discount)


# <----- Приклад використання поліморфізму клієнтським кодом ----->

def client_demo():
    # Динамічний поліморфізм через типи користувачів
    users = [Customer("cust1", "cust1@example.com"), Vendor("vend1", "vend1@example.com", "TechStore"), Admin("admin1", "admin@example.com")]

    for user in users:
        print(f"Тип користувача: {user.get_user_type()}")

    # Статичний поліморфізм через DiscountManager
    tv = Electronic("TV", 500.0, 2)
    sofa = Furniture("Sofa", 700.0, "Leather")
    shirt = Clothing("Shirt", 30.0, "L")

    discount_manager = DiscountManager()
    discount_manager.apply_bulk_discount([tv, sofa, shirt], 0.1)

    print(f"Ціна на телевізор після знижки: {tv.get_price()}")
    print(f"Ціна на диван після знижки: {sofa.get_price()}")
    print(f"Ціна на сорочку після знижки: {shirt.get_price()}")

# Запуск демонстрації клієнтського коду
client_demo()
