cart = []
# n = int(input('Enter the number of items you would like to input into the cart'))
#
# for x in range(n):
#     item = input('Enter an item into the cart: ')
#     cart.append(item)
#     print(cart)

while True:
    choice = input('Do you want to enter an item to the cart? (yes / no) \n>>>')
    if choice.lower() == "yes":
        item = input('Enter an item into the cart: ')
        cart.append(item)
        print(f"Current cart contents are {cart}")
    else:
        break
