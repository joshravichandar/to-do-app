# Create a ToDo App that connects to MySql - create new items, delete items
from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox
import mysql.connector


# connect to db using these credentials
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
        #TO_DO_ITEMS.append(item)
        #to_do_list.insert(len(TO_DO_ITEMS), item)
        add_to_db = ("INSERT INTO todo_list (item) "+"VALUES ('"+item+"');")
        cursor.execute(add_to_db)
        
        cnx.commit()
        new_item.set("")
        db_to_list()

def delete_press():
    # get selected item - string
    item = to_do_list.get(to_do_list.curselection())
    print(type(item))
    delete_from_db = ("DELETE FROM todo_list WHERE item= %s;")
    cursor.execute(delete_from_db, (item,))
    cnx.commit()

def on_close():
    db_to_list()
    if messagebox.askokcancel("QUIT", "Do you want to quit?"):
        cursor.close()
        cnx.close()
        root.destroy()


# set db into list
def db_to_list():
    all_items = ("SELECT * FROM TODO_LIST;")
    cursor.execute(all_items)
    records = cursor.fetchall()
    for i in records:
        #parsed = (i[2:len(i)-3])
        #print(parsed)
        #print("i = ", i)
        TO_DO_ITEMS.append(i[0])
        #pass

    # some print with {} - FIX THIS!
    to_do_set = set(TO_DO_ITEMS)
    for j in to_do_set:
        #TO_DO_ITEMS.append(j)
        to_do_list.insert(len(TO_DO_ITEMS), j)
        print("j = " + j)
    
    print(TO_DO_ITEMS)
    #return(to_do_set)

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
    delete = tk.Button(main_frame,width=20, text="Delete",command=delete_press).grid(column=0, row=8)
    db_to_list()

    # handle closing - > call on_close
    #root.protocol("WM_DELETE_WINDOW", on_close())
    root.mainloop()



# Trying to fix add and delete - currently working on add
# ATTEMPTED WORKFLOW: add press -> add to db -> add to list -> add to listbox GUI
# currently it goes: add press -> add to db -> reprint everything into gui???????