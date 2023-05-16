# First function creation
# def hello():
#     print("Bye")
#     print("Hi")
#     print("Tom")
#
#
# hello()

# Passing arguments to a function
# def add(a, b):
#     print(a+b)
#
#
# add(1, 2)

# Key word arguments
# def speed(distance, time):
#     print(distance / time)
#
#
# speed(distance=100, time=2)

# Default parameters
# def area(radius, pi=3.14):
#     print(pi*radius*radius)
#
#
# area(10)


# Making a function return a value

def area(radius, pi=3.14):
    result = pi*radius*radius
    return result


def cost(circle_area, cost_per_sqm):
    total_cost = circle_area*cost_per_sqm
    return total_cost


calculated_area = area(10, 3.15)
tc = cost(calculated_area, 2)
print(tc)
