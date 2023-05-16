# Opening a file

# Reading data
# file = open('data.txt', 'r')
# content = file.readline()
# print(content)
# file.close()

# Writing to a file
file = open('data.txt', 'a')
content = '\nThis is a third line'
file.write(content)
file.close()
