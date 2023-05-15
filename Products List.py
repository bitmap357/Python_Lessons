# Listing out the products with the product names, prices and descriptions in a list containing dictionaries.
products = [
    {"name": "Smartphone", "price": 500, "description": "A handheld device"},
    {"name": "Tablet", "price": 700, "description": "A larger handheld device"},
    {"name": "Laptop", "price": 1000, "description": "A portable computer that can rest on your lap"},
    {"name": "Headphones", "price": 50, "description": "A pair of earphones worn over the head to listen to music"},
    {"name": "Smartwatch", "price": 300, "description": "A device used for fitness tracking"}
]
# Declaring an empty list to store items the user would want to buy
cart = []

# The initialization of the loop that constantly asks the user if they would like to add another item
while True:
    choice = input('Do you want to continue shopping? \n>>>')
#   The check to verify the users choice and to either teminate the program or continue running it
    if choice.lower() == "yes":
        print('Here is a list of products and their prices')
#       Displaying each product available along with the description and the price.
#       The index was also added to ensure that the user gets an easy time while selecting an item.
        for index, product in enumerate(products):
            print(f"{index}: {product['name']}: {product['description']}: ${product['price']}")
        product_id = int(input("Enter the id of the product yu want to add to the cart:- "))

#       Check if product is already present in cart.
#       If it is, it adds another one to the already existing number, if not, it adds one to the quantity
        if products[product_id] in cart:
            products[product_id]['quantity'] += 1
        else:
            products[product_id]['quantity'] = 1
            cart.append(products[product_id])

#       Displaying the total items in the cart and calculating the total cost for all items in the cart.
        total = 0
        print(f"Current cart contains {cart}")
        for product in cart:
            print(f"{product['name']}: ${product['price']}: Quantity = {product['quantity']}")
            total = total + product['price'] * product['quantity']
        print(f"Cart total is: ${total}")
    else:
        break


print(f"Thank you, your current cart contents are {cart}")
