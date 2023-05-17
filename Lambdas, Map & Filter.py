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
# numbers = ['1', '2', '3', '4', '5']
#
# new_list = list(map(int, numbers))
# print(new_list)
#
# prices = [100, 200, 300, 400, 500]
#
# result = list(map(lambda x: x - x*5/100, prices))
# print(result)

# names = ['john', 'rob', 'mike']
# cap_names = list(map(str.capitalize, names))
# print(cap_names)

# Filters
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
# print(odd_numbers)


# Generator functions

# def function():
#     counter = 0
#     while counter <= 10:
#         yield counter
#         counter += 1
#
#
# print(list(function()))

def even_generator(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_generator(11)))

