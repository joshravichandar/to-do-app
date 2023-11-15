# Create a ToDo App that connects to MySql - create new items, delete items
from tkinter import *
from tkinter import ttk as tk

GLOBAL_ITEMS = []

# https://tkdocs.com/tutorial/morewidgets.html
# link to tkinter docs for setting listbox
def add_press(added_item, gl_items):
    gl_items = GLOBAL_ITEMS
    gl_items.append(added_item)
    added_item.set(gl_items)
    
    pass

def delete_press():
    pass

def up_press():
    pass

def down_press():
    pass




if __name__ == '__main__':
    root = Tk()
    root.title("To Do Application")
    main_frame = tk.Frame(root, padding="5 10 5 5")
    main_frame.grid()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    

    # create list and add to grid
    
    items = GLOBAL_ITEMS
    ITEMS_STRING = StringVar(value=items)
    to_do_list = Listbox(main_frame, width=20, listvariable=ITEMS_STRING)
    to_do_list.grid(column=0, row=0,rowspan=5 ,pady=5)
    ITEMS_STRING.set(items)
    

    # create var for entering new item, text field, add to grid
    new_item = StringVar(value=GLOBAL_ITEMS)
    enter_item = tk.Entry(main_frame, width=20, textvariable=new_item, justify=CENTER)
    enter_item.grid(column=0, row=6)

    # create all buttons and add to grid
    add = tk.Button(main_frame,width=20 ,text="Add Item",command=lambda: add_press(new_item, items)).grid(column=0, row=7)
    delete = tk.Button(main_frame, text="Delete").grid(column=1, row=3)
    up = tk.Button(main_frame, text="Up").grid(column=1, row=0)
    down = tk.Button(main_frame, text="Down").grid(column=1, row=1)

    root.mainloop()
