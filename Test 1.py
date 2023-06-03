from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import sqlite3
from tkinter.filedialog import askopenfile
import datetime
import os


dic = {}


def upload_file_com():
    """Upload a file to the database."""

    # Get the file path from the user.
    file_path = filedialog.askopenfilename(
        filetypes=[("TXT files", ".txt"), ("DOC files", ".doc"), ("DOCX files", ".docx"), ("PDF files", ".pdf")])

    # Check if the user selected a file.
    if file_path:

        # Get the file name and data.
        file_name = Path(file_path).name
        file_data = open(file_path, 'rb').read()
        # Get the file size.
        file_size = file_size_mb(file_path)
        tag = category1.get()

        # Update the choose_file_label with the file name.
        choose_file_label.config(text=file_name)

        # Insert the file into the treeview.
        trv.insert('', 'end', values=(category1.get(), file_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                      file_size))
        global dic
        dic = {
            "tag": tag,
            "file_name": file_name,
            "file": file_data,
            "file_size": file_size
        }

    else:

        # The user did not select a file.
        choose_file_label.config(text="NO FILE CHOSEN")


def file_size_mb(file_path):
    size_bytes = os.path.getsize(file_path)
    size_mb = size_bytes / (1024 * 1024)
    return size_mb


def change_to_main():
    """Switch to the main screen."""

    # Hide all frames except the main frame.
    upload.pack_forget()
    category.pack_forget()
    search.pack_forget()
    main.pack(fill='both', expand=1)


def change_to_upload():
    """Switch to the upload screen."""

    # Hide all frames except the upload frame.
    main.pack_forget()
    category.pack_forget()
    search.pack_forget()
    upload.pack(fill='both', expand=1)


def change_to_category():
    """Switch to the category screen."""

    # Hide all frames except the category frame.
    main.pack_forget()
    upload.pack_forget()
    search.pack_forget()
    category.pack(fill='both', expand=1)


def change_to_search():
    """Switch to the search screen."""

    # Hide all frames except the search frame.
    main.pack_forget()
    upload.pack_forget()
    category.pack_forget()
    search.pack(fill='both', expand=1)


def save(tag, file_name, file, file_size):
    """Save a file to the database."""

    # Get the current timestamp.
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert into table
    with sqlite3.connect('test.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO files (tag, file_name, file, date, size) VALUES (?, ?, ?, ?, ?)",
                  (tag, file_name, file, timestamp, file_size))
        conn.commit()


def search_files():
    """Search for files in the database."""

    # Clear existing treeview items.
    trv.delete(*trv.get_children())

    # Get the search keyword from the entry.
    keyword = search_entry.get()

    # Create a database connection and cursor.
    with sqlite3.connect('test.db') as conn:
        c = conn.cursor()

        # Fetch records matching the search keyword.
        c.execute("SELECT * FROM files WHERE file_name LIKE ?", ('%' + keyword + '%',))
        records = c.fetchall()

        # Insert records into the treeview.
        for record in records:
            trv.insert('', 'end', values=record)

    # Close the database connection.
    conn.close()


# Create the main window.
root = Tk()
root.geometry('880x500')
root.title('File Upload')

# Create the frames.
main = Frame(root)
upload = Frame(root)
category = Frame(root)
search = Frame(root)

# Pack the main frame.
main.pack(fill='both', expand=1)

# Create the labels and buttons.
home_button = Button(root, text='HOME', font=('Georgia', '14'), command=change_to_main)
home_button.place(relx=0, rely=0)

# Welcome text on the main screen.
main_label = Label(main, text='WELCOME\n WHAT WOULD YOU LIKE TO DO TODAY?', font=('Times New Roman', '32'))
main_label.place(relx=0, rely=0)
main_label.grid(pady=20, padx=10)

# Button for file uploads.
upload_file_button = Button(main, text='UPLOAD FILE', pady=20, padx=40, command=change_to_upload)
upload_file_button.grid(row=2, column=0, padx=10, pady=10)

# Button for browsing files.
browse_files_button = Button(main, text='BROWSE FILES', pady=20, padx=40, command=change_to_category)
browse_files_button.grid(row=3, column=0, padx=10, pady=10)

# Upload Screen
file_upload_label = Label(upload, text='FILE UPLOAD', font=('Times New Roman', '32'))
file_upload_label.place(relx=0.5, rely=0.1, anchor=CENTER)

choose_file_button = Button(upload, text='CHOOSE FILE', padx=10, pady=3, command=upload_file_com)
choose_file_button.place(relx=0.01, rely=0.25, anchor=W)

choose_file_label = Label(upload, text="", borderwidth=1, relief='solid', padx=180, pady=6)
choose_file_label.place(relx=0.13, rely=0.22)

frame_1 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
frame_1.place(relx=0.3, rely=0.3)

category_label = Label(frame_1, text='SELECT CATEGORY', font=('Times New Roman', '18'), padx=30)
category_label.pack()

category1 = StringVar(value='Other')
internal_radio = Radiobutton(frame_1, text='Internal File', value='Internal', variable=category1,
                             font=('Times New Roman', '14'))
partners_radio = Radiobutton(frame_1, text='Partners File', value='Partners', variable=category1,
                             font=('Times New Roman', '14'))
non_partners_radio = Radiobutton(frame_1, text='Non-Partners File', value='Non-Partners File',  variable=category1,
                             font=('Times New Roman', '14'))
other_radio = Radiobutton(frame_1, text='Other File', value='Other', variable=category1, font=('Times New Roman', '14'))

internal_radio.pack(padx=10, pady=10)
partners_radio.pack(padx=10, pady=10)
non_partners_radio.pack(padx=10, pady=10)
other_radio.pack(padx=10, pady=10)

frame_2 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
frame_2.place(relx=0.55, rely=0.3)

save_button = Button(upload, text='SAVE', padx=150, pady=3, command=lambda: save(tag=category1.get(), file_name="file_name", file="file_data"))
save_button.place(relx=0.3, rely=0.9)

# Category Screen
categories_label = Label(category, text='CATEGORIES', font=('Times New Roman', '32'))
categories_label.place(relx=0.5, rely=0.1, anchor=CENTER)

internal_button = Button(category, text='INTERNAL', padx=110, pady=50, command=change_to_search)
internal_button.place(relx=0.16, rely=0.2)

partners_button = Button(category, text='PARTNERS', padx=90, pady=50, command=change_to_search)
partners_button.place(relx=0.5, rely=0.2)

non_partners_button = Button(category, text='NON-PARTNERS', padx=90, pady=50, command=change_to_search)
non_partners_button.place(relx=0.16, rely=0.6)

other_button = Button(category, text='OTHER', padx=120, pady=50, command=change_to_search)
other_button.place(relx=0.5, rely=0.6)

search_label = Label(search, text='SEARCH FILES', font=('Times New Roman', '32'))
search_label.place(relx=0.5, rely=0.1, anchor=CENTER)

search_entry = Entry(search, font=('Times New Roman', '14'), width=40)
search_entry.place(relx=0.4, rely=0.2, anchor=CENTER)

search_button = Button(search, text='SEARCH', padx=50, pady=3, command=search_files)
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

# Start the main loop.
root.mainloop()
