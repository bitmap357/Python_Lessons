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
class Product:
    quantity = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price


p1 = Product("Phone", "300")
print(p1.name)
print(p1.price)

p2 = Product("Laptop", "900")
print(p2.name)
print(p2.price)



