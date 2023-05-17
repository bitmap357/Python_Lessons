# Lambda functions
# result = (lambda x: x**2)(7)
# print(result)

# result = (lambda x=10, y=20: x+y)(y=50)
# print(result)

# Map functions
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x*x


new_list = list(map(square, numbers))
print(new_list)