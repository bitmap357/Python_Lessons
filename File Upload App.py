from tkinter import *

# root = Tk()
# root.geometry('880x500')
#
# main_label = Label(root, text='WELCOME\n WHAT WOULD YOU LIKE TO DO TODAY?', font=('Times New Roman', '32'))
# main_label.grid(row=0, column=0, pady=20, padx=10)
#
# upload_file_button = Button(root, text='UPLOAD FILE', pady=20, padx=40)
# upload_file_button.grid(row=2, column=0, padx=10, pady=10)
#
# browse_files_button = Button(root, text='BROWSE FILES', pady=20, padx=40)
# browse_files_button.grid(row=3, column=0, padx=10, pady=10)
#
# root.mainloop()

upload_screen = Tk()
upload_screen.geometry('880x500')
file_upload_label = Label(upload_screen, text='FILE UPLOAD', font=('Times New Roman', '32'), anchor=CENTER)
# file_upload_label.place(relx=0.5, rely=0.5, anchor=CENTER)
file_upload_label.grid(row=0, column=5, pady=20, padx=10)


upload_screen.mainloop()