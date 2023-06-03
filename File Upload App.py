import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import datetime
import sqlite3

root = Tk()
root.geometry('880x500')
root.title('File Upload')

# Creating database and cursor
conn = sqlite3.connect('file_upload.db')
c = conn.cursor()

# Create table

# c.execute('''CREATE TABLE files (
#             tag text,
#             file_name text,
#             file blob,
#             date text,
#             size text
#             )''')


main = Frame(root)
upload = Frame(root)
category = Frame(root)
search = Frame(root)
main.pack()



def upload_file_com():
    file_path = filedialog.askopenfilename(
        filetypes=[("TXT files", ".txt"), ("DOC files", ".doc"), ("DOCX files", ".docx"), ("PDF files", ".pdf")])

    if file_path:
        # fob = open(file).read()
        # preview.insert(END, fob)
        file_name = Path(file_path).stem
        file_data = open(file_path, 'r').read()
        choose_file_label.config(text=file_name)
        trv.insert('', 'end', values=(category1.get(), file_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), len(file_data)))

    else:
        choose_file_label.config(text="NO FILE CHOSEN")


def change_to_main():
    main.pack(fill='both', expand=1)
    upload.pack_forget()
    category.pack_forget()
    search.pack_forget()


def change_to_upload():
    upload.pack(fill='both', expand=1)
    category.pack_forget()
    search.pack_forget()
    main.pack_forget()


def change_to_category():
    category.pack(fill='both', expand=1)
    upload.pack_forget()
    search.pack_forget()
    main.pack_forget()


def change_to_search_all():
    search.pack(fill='both', expand=1)
    category.pack_forget()
    upload.pack_forget()
    main.pack_forget()


def change_to_search_in():
    search.pack(fill='both', expand=1)
    category.pack_forget()
    upload.pack_forget()
    main.pack_forget()


def change_to_search_par():
    search.pack(fill='both', expand=1)
    category.pack_forget()
    upload.pack_forget()
    main.pack_forget()


def change_to_search_non():
    search.pack(fill='both', expand=1)
    category.pack_forget()
    upload.pack_forget()
    main.pack_forget()


def change_to_search_oth():
    search.pack(fill='both', expand=1)
    category.pack_forget()
    upload.pack_forget()
    main.pack_forget()


def save(tag, file_name, file, timestamp, size):
    # Create a database or connect to one
    conn = sqlite3.connect('file_upload.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO  files VALUES (:tag, :file_name, :file, :date, :size)",
              {
                  'tag': tag,
                  'file_name': file_name,
                  'file': file,
                  'date': timestamp,
                  'size': size
              })
    # c.execute("INSERT INTO  files VALUES (?, ?, ?, ?, ?)", (tag, file_name, file, date, size))

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    # # Clear text boxes
    # f_name.delete(0, END)
    # l_name.delete(0, END)
    # address.delete(0, END)
    # city.delete(0, END)
    # state.delete(0, END)
    # zipcode.delete(0, END)


def search_files():
    """Search for files in the database."""

    # Clear existing treeview items.
    trv.delete(*trv.get_children())

    # Get the search keyword from the entry.
    keyword = search_entry.get()

    # Create a database connection and cursor.
    with sqlite3.connect('file_upload.db') as conn:
        c = conn.cursor()

    # Fetch records matching the search keyword.
        c.execute("SELECT * FROM files WHERE file_name LIKE ?", ('%' + keyword + '%',))
        records = c.fetchall()

        # Insert records into the treeview.
        for record in records:
            trv.insert('', 'end', values=record)

        # Close the database connection.
    conn.close()


home_button = Button(root, text='HOME', font=('Georgia', '14'), command=change_to_main)
home_button.place(relx=0, rely=0)


# Welcome text on the main screen
main_label = Label(main, text='WELCOME\n WHAT WOULD YOU LIKE TO DO TODAY?', font=('Times New Roman', '32'))
main_label.place(relx=0, rely=0)
main_label.grid(pady=20, padx=10)

# Button for file uploads
upload_file_button = Button(main, text='UPLOAD FILE', pady=20, padx=40, command=change_to_upload)
upload_file_button.grid(row=2, column=0, padx=10, pady=10)

# Button for browsing files
browse_files_button = Button(main, text='BROWSE FILES', pady=20, padx=40, command=change_to_category)
browse_files_button.grid(row=3, column=0, padx=10, pady=10)


# Upload Screen
file_upload_label = Label(upload, text='FILE UPLOAD', font=('Times New Roman', '32'))
file_upload_label.place(relx=0.5, rely=0.1, anchor=CENTER)

choose_file_button = Button(upload, text='CHOOSE FILE', padx=10, pady=3, command=lambda: upload_file_com())
choose_file_button.place(relx=0.01, rely=0.25, anchor=W)


choose_file_label = Label(upload, text="", borderwidth=1, relief='solid', padx=180, pady=6)
choose_file_label.place(relx=0.13, rely=0.22)

frame_1 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
frame_1.place(relx=0.3, rely=0.3)

category_label = Label(frame_1, text='SELECT CATEGORY', font=('Times New Roman', '18'), padx=30)
category_label.pack()

category1 = StringVar(value='Other')
internal_radio = Radiobutton(frame_1, text='Internal File', value='Internal', variable=category1, font=('Times New Roman', '14'))
partners_radio = Radiobutton(frame_1, text='Partners File', value='Partners', variable=category1, font=('Times New Roman', '14'))
non_partners_radio = Radiobutton(frame_1, text='Non-Partners File', value='Non-Partners', variable=category1, font=('Times New Roman', '14'))
other_radio = Radiobutton(frame_1, text='Other File', value='Other', variable=category1, font=('Times New Roman', '14'))


internal_radio.pack(padx=10, pady=10)
partners_radio.pack(padx=10, pady=10)
non_partners_radio.pack(padx=10, pady=10)
other_radio.pack(padx=10, pady=10)

frame_2 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
frame_2.place(relx=0.55, rely=0.3)

# description_label = Label(frame_2, text='DESCRIPTION', font=('Times New Roman', '18'), padx=80)
# description_label.pack()
#
# description_input = Entry(frame_2, width=30, border=2, font=('Times New Roman', '14'))
# description_input.pack()

save_button = Button(upload, text='SAVE', padx=150, pady=3)
save_button.place(relx=0.3, rely=0.9)


# Category Screen
categories_label = Label(category, text='CATEGORIES', font=('Times New Roman', '32'))
categories_label.place(relx=0.5, rely=0.1, anchor=CENTER)

internal_button = Button(category, text='INTERNAL', padx=110, pady=50, command=change_to_search_in)
internal_button.place(relx=0.16, rely=0.2)

partners_button = Button(category, text='PARTNERS', padx=90, pady=50, command=change_to_search_par)
partners_button.place(relx=0.5, rely=0.2)

non_partners_button = Button(category, text='NON-PARTNERS', padx=90, pady=50, command=change_to_search_non)
non_partners_button.place(relx=0.16, rely=0.55)

other_button = Button(category, text='OTHER', padx=100, pady=50, command=change_to_search_oth)
other_button.place(relx=0.5, rely=0.55)

all_button = Button(category, text='ALL', padx=258, pady=15, command=change_to_search_all)
all_button.place(relx=0.16, rely=0.85)


# Search Screen
search_label = Label(search, text='SEARCH FILES', font=('Times New Roman', '32'))
search_label.place(relx=0.5, rely=0.1, anchor=CENTER)

search_entry = Entry(search, font=('Times New Roman', '14'), width=40)
search_entry.place(relx=0.4, rely=0.2, anchor=CENTER)

search_button = Button(search, text='SEARCH', padx=50, pady=3)  # command=search_files)
search_button.place(relx=0.7, rely=0.2, anchor=CENTER)

trv = ttk.Treeview(search, columns=('1', '2', '3', '4'), show="headings", height=15)
trv.place(relx=0.5, rely=0.6, anchor=CENTER)

trv.heading(1, text="Tag")
trv.column(1, width=100, anchor=CENTER)
trv.heading(2, text="File Name")
trv.column(2, width=300, anchor=CENTER)
trv.heading(3, text="Date")
trv.column(3, width=100, anchor=CENTER)
trv.heading(4, text="Size")
trv.column(4, width=100, anchor=CENTER)

scroll = ttk.Scrollbar(search, orient='vertical', command=trv.yview)
scroll.place(relx=0.95, rely=0.5, anchor=E)
trv.configure(yscrollcommand=scroll.set)


root.mainloop()

