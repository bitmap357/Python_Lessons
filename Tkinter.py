from tkinter import *


# def display():
#     data = entry.get()
#     print(data)

# def add():
#     n1 = int(number1.get())
#     n2 = int(number2.get())
#     result = str(n1+n2)
#     answer.config(text='Answer is: ' + result)

# def selected():
#     label.config(text=check_value.get())


# root = Tk()
# root.geometry('300x300')
# Label
# hello = Label(root, text='Hello World', fg='red', bg='white', font=('Ariel', 16))
# hello.pack()

# User input
# entry = Entry(root)
# entry.pack()

# Button
# button = Button(root, text='Click here', command=display)
# button.pack()

# Adding 2 numbers
# number1 = Entry(root)
# number2 = Entry(root)
# number1.pack()
# number2.pack()
#
# button = Button(root, text='Add', command=add)
# button.pack()
#
# answer = Label(root)
# answer.pack()

# Checkboxes
# check_value = BooleanVar()
# checkbutton = Checkbutton(root, text='Accept terms', variable=check_value, command=selected)
# checkbutton.pack()
#
# label = Label(root)
# label.pack()
#
#
# root.mainloop()

# Beverage Selector
# def selected():
#     sugar = sugar_var.get()
#     ice = ice_var.get()
#     cream = cream_var.get()
#     if sugar:
#         sugar = "Sugar"
#     else:
#         sugar = 'No Sugar'
#     if ice:
#         ice = "Ice"
#     else:
#         ice = 'No Ice'
#     if cream:
#         cream = "Cream"
#     else:
#         cream = 'No Cream'
#
#     label.config(text='Options selected are:' + "\n" + sugar + "\n" + ice + "\n" + cream)
#
#
# root = Tk()
# root.geometry('300x300')
#
# sugar_var = BooleanVar()
# ice_var = BooleanVar()
# cream_var = BooleanVar()
#
# sugar_checkbox = Checkbutton(root, text='Sugar', variable=sugar_var, command=selected)
# ice_checkbox = Checkbutton(root, text='Ice', variable=ice_var, command=selected)
# cream_checkbox = Checkbutton(root, text='Cream', variable=cream_var, command=selected)
#
# label = Label(root)
#
# sugar_checkbox.pack()
# ice_checkbox.pack()
# cream_checkbox.pack()
# label.pack()
#
# root.mainloop()

# Radio buttons
# def selected():
#     label.config(text='Choice of fuel is: ' + fuel.get())
#
#
# root = Tk()
# root.geometry('300x300')
#
# fuel = StringVar(value='Petrol')
#
# radio1 = Radiobutton(root, text='Petrol', variable=fuel, value='Petrol', command=selected)
# radio2 = Radiobutton(root, text='Diesel', variable=fuel, value='Diesel', command=selected)
# radio3 = Radiobutton(root, text='Electric', variable=fuel, value='Electric', command=selected)
#
# label = Label(root)
# radio1.pack()
# radio2.pack()
# radio3.pack()
# label.pack()
# root.mainloop()

# Frames

# root = Tk()
# frame = Frame(root, highlightthickness=1, highlightbackground='white', padx="20", pady="20")
# frame.pack()
#
# frame2 = Frame(root)
# frame2.pack(side=BOTTOM)
#
# button = Button(frame, text='Button1')
# button2 = Button(frame2, text='Button2')
#
# button.pack()
# button2.pack()
#
# root.geometry('300x300')
#
# root.mainloop()

# Grid Layout
# root = Tk()
# label1 = Label(root, text='Email')
# label2 = Label(root, text='Password')
#
# text1 = Entry(root)
# text2 = Entry(root)
#
# label1.grid(row=0, column=0)
# text1.grid(row=0, column=1)
#
# label2.grid(row=1, column=0)
# text2.grid(row=1, column=1)
#
# button = Button(root, text='Login')
# button.grid(column=1, row=2)
#
# root.geometry('300x300')
#
# root.mainloop()

# Crating a Grid
root = Tk()
for x in range(3):
    for y in range(3):
        frame = Frame(root)
        frame.grid(row=x, column=y)
        button = Button(frame, text=f'Row {x} \n Column {y}')
        button.pack(pady=5, padx=5)

root.mainloop()
