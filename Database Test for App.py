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

# Create text box labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zip code')
zipcode_label.grid(row=5, column=0)

# Commit changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()
