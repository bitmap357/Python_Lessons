from tkinter import *
import sqlite3

root = Tk()
root.geometry('400x400')

# Databases
# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table

# c.execute('''CREATE TABLE addresses (
#             first_name text,
#             last_name text,
#             address text,
#             city text,
#             state text,
#             zipcode integer
#             )''')

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Commit changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()
