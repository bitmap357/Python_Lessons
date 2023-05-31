from tkinter import *
# from tkinter import font

# root = Tk()
# root.geometry('880x500')
#
# greet = Frame(root)
# order = Frame(root)
#
#
# def change_to_greet():
#     greet.pack(fill='both', expand=1)
#     order.pack_forget()
#
#
# def change_to_order():
#     order.pack(fill='both', expand=1)
#     greet.pack_forget()
#
#
# # Create fonts for making difference in the frame
# font1 = font.Font(family='Georgia', size=22, weight='bold')
# font2 = font.Font(family='Aerial', size=12)
#
# # Add a heading logo in the frames
# label1 = Label(greet, text="Hey There! Welcome to TutorialsPoint.", foreground="green3", font=font1)
# label1.pack(pady=20)
#
# label2 = Label(order, text="Find all the interesting Tutorials.", foreground="blue", font=font2)
# label2.pack(pady=20)
#
# # Add a button to switch between two frames
# btn1 = Button(root, text="Switch to Greet", font=font2, command=change_to_order)
# btn1.pack(pady=20)
#
# btn2 = Button(order, text="Switch to Order", font=font2, command=change_to_greet)
# btn2.pack(pady=20)
#
# root.mainloop()


def scankey(event):
    val = event.widget.get()
    print(val)

    if val == '':
        data = list1
    else:
        data = []
        for item in list1:
            if val.lower() in item.lower():
                data.append(item)

    update(data)


def update(data):
    listbox.delete(0, 'end')

    # put new data
    for item in data:
        listbox.insert('end', item)


list1 = ('C', 'C++', 'Java', 'Python', 'Perl', 'PHP', 'ASP', 'JS')

ws = Tk()

entry = Entry(ws)
entry.pack()
entry.bind('<KeyRelease>', scankey)

listbox = Listbox(ws)
listbox.pack()
update(list1)

ws.mainloop()
