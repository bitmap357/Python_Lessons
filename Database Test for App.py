from tkinter import *
import sqlite3

root = Tk()
root.geometry('400x400')

# Databases
# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

c = conn.cursor()




root.mainloop()
