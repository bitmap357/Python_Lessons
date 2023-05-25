from tkinter import *

root = Tk()

main_label = Label(root, text='WELCOME\n WHAT WOULD YOU LIKE TO DO TODAY?', font=('Times New Roman', '32'))
main_label.grid(row=0, column=0)

upload_file_button = Button(root, text='UPLOAD FILE')

root.mainloop()
