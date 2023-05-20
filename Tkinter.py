from tkinter import *


def display():
    data = entry.get()
    print(data)


root = Tk()
root.geometry('300x300')
# Label
# hello = Label(root, text='Hello World', fg='red', bg='white', font=('Ariel', 16))
# hello.pack()

# User input
entry = Entry(root)
entry.pack()

# Button
button = Button(root, text='Click here', command=display)
button.pack()


root.mainloop()
