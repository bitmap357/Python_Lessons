from tkinter import *

# root = Tk()
# root.geometry('880x500')
#
# # Welcome text on the main screen
# main_label = Label(root, text='WELCOME\n WHAT WOULD YOU LIKE TO DO TODAY?', font=('Times New Roman', '32'))
# main_label.grid(row=0, column=0, pady=20, padx=10)
#
# # Button for file uploads
# upload_file_button = Button(root, text='UPLOAD FILE', pady=20, padx=40)
# upload_file_button.grid(row=2, column=0, padx=10, pady=10)
#
# # Button for browsing files
# browse_files_button = Button(root, text='BROWSE FILES', pady=20, padx=40)
# browse_files_button.grid(row=3, column=0, padx=10, pady=10)
#
# root.mainloop()
#
#
# # Second screen for uploading of files
# upload_screen = Tk()
# upload_screen.geometry('880x500')
#
#
# file_upload_label = Label(upload_screen, text='FILE UPLOAD', font=('Times New Roman', '32'))
# file_upload_label.place(relx=0.5, rely=0.1, anchor=CENTER)
#
# choose_file_button = Button(upload_screen, text='CHOOSE FILE', padx=10, pady=3)
# choose_file_button.place(relx=0.01, rely=0.25, anchor=W)
#
#
# choose_file_label = Label(upload_screen, text='dummy file name', borderwidth=1, relief='solid', padx=330, pady=6)
# choose_file_label.place(relx=0.13, rely=0.22)
#
# frame_1 = Frame(upload_screen, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
# frame_1.place(relx=0.05, rely=0.3)
#
# category_label = Label(frame_1, text='SELECT CATEGORY', font=('Times New Roman', '18'), padx=30)
# category_label.pack()
#
# category = StringVar(value='None')
# internal_radio = Radiobutton(frame_1, text='Internal File', value='Internal', variable=category, font=('Times New Roman', '14'))
# partners_radio = Radiobutton(frame_1, text='Partners File', value='Partners', variable=category, font=('Times New Roman', '14'))
# non_partners_radio = Radiobutton(frame_1, text='Non-Partners File', value='Non-Partners', variable=category, font=('Times New Roman', '14'))
# other_radio = Radiobutton(frame_1, text='Other File', value='Other', variable=category, font=('Times New Roman', '14'))
#
#
# internal_radio.pack(padx=10, pady=10)
# partners_radio.pack(padx=10, pady=10)
# non_partners_radio.pack(padx=10, pady=10)
# other_radio.pack(padx=10, pady=10)
#
# frame_2 = Frame(upload_screen, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
# frame_2.place(relx=0.55, rely=0.3)
#
# description_label = Label(frame_2, text='DESCRIPTION', font=('Times New Roman', '18'), padx=80)
# description_label.pack()
#
# description_input = Entry(frame_2, width=30, border=2, font=('Times New Roman', '14'))
# description_input.pack()
#
# save_button = Button(upload_screen, text='SAVE', padx=150, pady=3)
# save_button.place(relx=0.3, rely=0.9)
#
#
# upload_screen.mainloop()

# Category Screen
# category_screen = Tk()
# category_screen.geometry('880x500')
#
# categories_label = Label(category_screen, text='CATEGORIES', font=('Times New Roman', '32'))
# categories_label.place(relx=0.5, rely=0.1, anchor=CENTER)
#
# internal_button = Button(category_screen, text='INTERNAL', padx=60, pady=50)
# internal_button.place(relx=0.03, rely=0.2)
#
# partners_button = Button(category_screen, text='PARTNERS', padx=60, pady=50)
# partners_button.place(relx=0.4, rely=0.2)
#
# non_partners_button = Button(category_screen, text='NON-PARTNERS', padx=60, pady=50)
# non_partners_button.place(relx=0.72, rely=0.2)
#
# other_button = Button(category_screen, text='OTHER', padx=60, pady=50)
# other_button.place(relx=0.2, rely=0.55)
#
# back_button = Button(category_screen, text='BACK', padx=60, pady=50)
# back_button.place(relx=0.6, rely=0.55)
#
#
# category_screen.mainloop()

# Search Screen
search_screen = Tk()
search_screen.geometry('880x500')

search_label = Label(search_screen, text='SEARCH FILES', font=('Times New Roman', '32'))
search_label.place(relx=0.5, rely=0.1, anchor=CENTER)


search_screen.mainloop()
