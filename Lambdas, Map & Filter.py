# Lambda functions
# result = (lambda x: x**2)(7)
# print(result)

# result = (lambda x=10, y=20: x+y)(y=50)
# print(result)

# Map functions
# numbers = [1, 2, 3, 4, 5]
#
#
# def square(x):
#     return x*x
#
#
# new_list = list(map(square, numbers))
# print(new_list)

# Different ways of using map
numbers = ['1', '2', '3', '4', '5']

new_list = list(map(int, numbers))
print(new_list)

prices = [100, 200, 300, 400, 500]

result = list(map(lambda x: x - x*5/100, prices))
print(result)
