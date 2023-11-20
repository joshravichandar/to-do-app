# Create a ToDo App that connects to MySql - create new items, delete items
from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

# ADD BACK PASSWORD
cnx = mysql.connector.connect(user='admin', password='password', host='localhost', database='todoapp_db')
cursor = cnx.cursor()
print(cnx)

TO_DO_ITEMS = []

# https://tkdocs.com/tutorial/morewidgets.html
# link to tkinter docs for setting listbox
def add_press():
    # take in item string from entry field
    item = new_item.get()
    # append to list first, append from list to listbox, reset to empty
    if (item != ""):
        TO_DO_ITEMS.append(item)
        to_do_list.insert(len(TO_DO_ITEMS), item)
        add_from_db = ("INSERT INTO todo_list (item) "+"VALUES ('"+item+"');")
        cursor.execute(add_from_db)
        cnx.commit()
        new_item.set("")

        # WHERE DO WE CLOSE THIS STUFF
        cursor.close()
        cnx.close()

def delete_press():
    # get selected item
    item = to_do_list.get(to_do_list.curselection())
    delete_from_db = ("DELETE FROM todo_list WHERE item= '"+item+"';")
    cursor.execute(delete_from_db)
    cnx.commit()

def on_close():
    if messagebox.askokcancel("QUIT", "Do you want to quit?"):
        cursor.close()
        cnx.close()
        root.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title("To Do Application")
    main_frame = tk.Frame(root, padding="5 10 5 5")
    main_frame.grid()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    # create list and add to grid
    to_do_list = Listbox(main_frame, width=20)
    to_do_list.grid(column=0, row=0,rowspan=5 ,pady=5)
    
    # create var for entering new item, text field, add to grid
    new_item = StringVar(value=TO_DO_ITEMS)
    enter_item = tk.Entry(main_frame, width=20, textvariable=new_item, justify=CENTER)
    enter_item.grid(column=0, row=6)

    # create all buttons and add to grid
    add = tk.Button(main_frame,width=20 ,text="Add Item",command=add_press).grid(column=0, row=7)
    delete = tk.Button(main_frame, text="Delete").grid(column=1, row=3)
    up = tk.Button(main_frame, text="Up").grid(column=1, row=0)
    down = tk.Button(main_frame, text="Down").grid(column=1, row=1)

    # handle closing
    root.protocol("DELETE_WINDOW", on_close)
    root.mainloop()
