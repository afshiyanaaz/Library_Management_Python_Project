from tkinter import *
import backend

selected_tuple = None  # to store the selected record (id, title, author, year, isbn)


def get_selected_row(event):
    """When user selects a row in the listbox, fill the entry boxes."""
    global selected_tuple
    try:
        index = list1.curselection()[0]
        selected = list1.get(index)            # e.g. "11 | Harry Potter | J.K Rowling | 1999 | 1234"
        parts = selected.split(" | ")

        # convert back to tuple: (id, title, author, year, isbn)
        selected_tuple = (int(parts[0]), parts[1], parts[2], parts[3], parts[4])

        # fill the entries
        e1.delete(0, END)
        e1.insert(END, parts[1])

        e2.delete(0, END)
        e2.insert(END, parts[2])

        e3.delete(0, END)
        e3.insert(END, parts[3])

        e4.delete(0, END)
        e4.insert(END, parts[4])

    except IndexError:
        selected_tuple = None  # nothing selected


def view_command():
    """Show all books in the listbox with clean formatting."""
    list1.delete(0, END)
    for row in backend.view():
        # row = (id, title, author, year, isbn)
        display = f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}"
        list1.insert(END, display)


def search_command():
    """Search books and show results."""
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(),
                              year_text.get(), isbn_text.get()):
        display = f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}"
        list1.insert(END, display)


def add_command():
    """Add a new book."""
    if title_text.get().strip() == "" or author_text.get().strip() == "":
        return  # basic validation

    backend.insert(title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())

    # after inserting, just refresh the list
    view_command()
    clear_entries()


def delete_command():
    """Delete the selected book."""
    if selected_tuple:
        backend.delete(selected_tuple[0])
        view_command()


def update_command():
    """Update the selected book with current entry values."""
    if selected_tuple:
        backend.update(selected_tuple[0],
                       title_text.get(), author_text.get(),
                       year_text.get(), isbn_text.get())
        view_command()


def clear_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def close_command():
    window.destroy()


# ------------- GUI SETUP ------------- #

window = Tk()
window.title("Library Management System (Simple)")

# Labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Entry fields
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# Listbox
list1 = Listbox(window, height=10, width=60)
list1.grid(row=2, column=0, rowspan=6, columnspan=3)

# Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6, sticky='ns')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=4)

b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=3, column=4)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=4)

b4 = Button(window, text="Edit", width=12, command=update_command)
b4.grid(row=5, column=4)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=4)

b6 = Button(window, text="Close", width=12, command=close_command)
b6.grid(row=7, column=4)

window.mainloop()
