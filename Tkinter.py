from tkinter import *

def display():
    print('Button clicked')


root = Tk()
root.geometry('300x300')
# Label
# hello = Label(root, text='Hello World', fg='red', bg='white', font=('Ariel', 16))
# hello.pack()

# Button
button = Button(root, text='Click here', command=display)
button.pack()
root.mainloop()
