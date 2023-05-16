# Syntax errors: error with the construction of the codes
# Logical error: error with the functionality of the code
# Runtime error: error that occurs when the program is executing
# Try & except block

n = int(input('Enter numerator'))
d = int(input('Enter denominator'))
result = 0

try:
    result = n / d

except ZeroDivisionError:
    print("Cannot divide a number by zero")

# Else block
else:
    print(result)

# Finally block

