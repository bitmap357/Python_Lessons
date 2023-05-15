products = [
    {"name": "Smartphone", "price": 500, "description": "A handheld device"},
    {"name": "Tablet", "price": 700, "description": "A larger handheld device"},
    {"name": "Laptop", "price": 1000, "description": "A portable computer that can rest on your lap"},
    {"name": "Headphones", "price": 50, "description": "A pair of earphones worn over the head to listen to music"},
    {"name": "Smartwatch", "price": 300, "description": "A device used for fitness tracking"}
]

cart = []

while True:
    choice = input('Do you want to continue shopping? \n>>>')

    if choice.lower() == "yes":
        print('Here is a list of products and their prices')
        for index, product in enumerate(products):
            print(f"{index}: {product['name']}: {product['description']}: ${product['price']}")
        product_id = int(input("Enter the id of the product yu want to add to the cart:- "))

#       Check if product is already present in cart
        if products[product_id] in cart:
            products[product_id]['quantity'] += 1
        else:
            products[product_id]['quantity'] = 1
            cart.append(products[product_id])

        print(f"Current cart contains {cart}")
        for product in cart:
            print(f"{product['name']}: ${product['price']}: Quantity = {product['quantity']}")
    else:
        break


print(f"Thank you, your current cart contents are {cart}")
