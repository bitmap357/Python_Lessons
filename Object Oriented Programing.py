# Creating classes and objects
# class Product:
#     quantity = 200
#
#
# p1 = Product()
# print(p1.quantity)
#
# p2 = Product()
# print(p2.quantity)


# Creating instance attributes
# class Product:
#     quantity = 200
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# p1 = Product("Phone", "300")
# print(p1.name)
# print(p1.price)
#
# p2 = Product("Laptop", "900")
# print(p2.name)
# print(p2.price)


# Methods in OOP
# class Product:
#     quantity = 200
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def summer_discount(self, discount_percent):
#         self.price = self.price - self.price * discount_percent / 100
#
#
# p1 = Product("Tshirt", 10)
# print(p1.name)
# print(p1.price)
# p1.summer_discount(10)
# print(p1.price)
#
#
# p2 = Product('Phone', 400)
# p2.summer_discount(10)
# print(p2.price)


# Functional & OOP Based Way of Writing Code
# Functional way
# def product_data():
#     product_name = input('Enter name of the product')
#     product_price = input('Enter price of the product')
#     print(product_name)
#     print(product_price)
#
# product_data()

# OOP way
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_data(self):
        self.name = input('Enter name of the product')
        self.price = input('Enter price of the product')

    def put_data(self):
        print(self.name)
        print(self.price)


p1 = Product("", "")
p1.get_data()
p1.put_data()
