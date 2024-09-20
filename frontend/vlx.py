import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def switch_frame(frame):
    frame.tkraise()

def show_selection(value):
    global categories_selected
    categories_selected = value

def submitadd():
    item = entry_add_item.get()
    price = entry_add_price.get()
    desc = entry_add_desc.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not price.isdigit():
        messagebox.showerror("Error", "Invalid price. Please enter a numeric value.")
        return
    print([item, categories_selected, price, desc, timestamp])

def submitsearch():
    item = entry_search_item.get()
    print([item, categories_selected])

root = tk.Tk()
root.configure(bg='lightgrey')
root.geometry("1200x800")
root.title('VLX')

main_frame = tk.Frame(root, bg='lightgrey')
search_frame = tk.Frame(root, bg='lightgrey')
add_frame = tk.Frame(root, bg='lightgrey')

for frame in (search_frame, add_frame, main_frame):
    frame.grid(row=0, column=0, sticky="nsew")

selected_option = tk.StringVar(root)
selected_option.set("Choose Category")
categories = ["Electronics", "Stationary", "Sports", "Fashion", "Foods and Beverages"]

# Add Item Frame
item_add_label = tk.Label(add_frame, text='Item Name', bg='lightgrey', fg='black', font=('Arial', 14))
item_add_label.pack(pady=10)
entry_add_item = tk.Entry(add_frame, width=30, font=('Arial', 14))
entry_add_item.pack(pady=5)

categories_add_label = tk.Label(add_frame, text='Item Category', bg='lightgrey', fg='black', font=('Arial', 14))
categories_add_label.pack(pady=10)
dropdown_add = tk.OptionMenu(add_frame, selected_option, *categories, command=show_selection)
dropdown_add.pack(pady=5)

price_add_label = tk.Label(add_frame, text='Item Price', bg='lightgrey', fg='black', font=('Arial', 14))
price_add_label.pack(pady=10)
entry_add_price = tk.Entry(add_frame, width=30, font=('Arial', 14))
entry_add_price.pack(pady=5)

desc_add_label = tk.Label(add_frame, text='Item Description', bg='lightgrey', fg='black', font=('Arial', 14))
desc_add_label.pack(pady=10)
entry_add_desc = tk.Entry(add_frame, width=30, font=('Arial', 14))
entry_add_desc.pack(pady=5)

submit_add_button = tk.Button(add_frame, text="Submit", command=submitadd)
submit_add_button.pack(pady=10)

back_button_add = tk.Button(add_frame, text="Back", command=lambda: switch_frame(main_frame))
back_button_add.pack(pady=10)

# Search Item Frame
item_search_label = tk.Label(search_frame, text="Enter Item Name", bg='lightgrey', fg='black', font=('Arial', 14))
item_search_label.pack(pady=10)
entry_search_item = tk.Entry(search_frame, width=30, font=("Arial", 14))
entry_search_item.pack(pady=5)

categories_search_label = tk.Label(search_frame, text='Item Category', bg='lightgrey', fg='black', font=('Arial', 14))
categories_search_label.pack(pady=10)
dropdown_search = tk.OptionMenu(search_frame, selected_option, *categories, command=show_selection)
dropdown_search.pack(pady=5)

submit_search_button = tk.Button(search_frame, text="Submit", command=submitsearch)
submit_search_button.pack(pady=10)

back_button_search = tk.Button(search_frame, text="Back", command=lambda: switch_frame(main_frame))
back_button_search.pack(pady=10)

# Main Frame
main_label = tk.Label(main_frame, text="WELCOME TO VLX", bg='lightgrey', fg='black', font=('Arial', 24))
main_label.pack(pady=20)

add_button = tk.Button(main_frame, text="Add Item", command=lambda: switch_frame(add_frame))
add_button.pack(pady=10)

search_button = tk.Button(main_frame, text="Search Item", command=lambda: switch_frame(search_frame))
search_button.pack(pady=10)

switch_frame(main_frame)
root.mainloop()
