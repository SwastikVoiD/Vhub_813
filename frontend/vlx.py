import tkinter as tk
from tkinter import messagebox
def switch_frame(frame):
    frame.tkraise()
def show_selection(value):
    global categories_selected
    categories_selected = value

def check():
    item = entry_add_item.get()
    price = entry_add_price.get()
    desc = entry_add_desc.get()
    if not price.isdigit():
        messagebox.showerror("Error", "Invalid price. Please enter a numeric value.")
        return
    print([item, categories_selected, price, desc])

root = tk.Tk()
root.configure(bg='lightgrey')
root.geometry("1200x800")
root.title('OLX')

main_frame=tk.Frame(root,bg='lightgrey')
search_frame = tk.Frame(root, bg='lightgrey')
add_frame = tk.Frame(root, bg='lightgrey')

for frame in (search_frame, add_frame):
    frame.grid(row=0, column=0, sticky="nsew")

selected_option = tk.StringVar(root)
selected_option.set("Choose Category")
categories = ["Electronics", "Stationary"]

item_add_label = tk.Label(add_frame, text='Item Name', bg='lightgrey', fg='black', font=('Arial', 14))
item_add_label.pack(pady=20)
entry_add_item = tk.Entry(add_frame, width=30, font=('Arial', 14))
entry_add_item.pack(pady=5)

categories_add_label = tk.Label(add_frame, text='Item Category', bg='lightgrey', fg='black', font=('Arial', 14))
categories_add_label.pack(pady=20)
dropdown_add = tk.OptionMenu(add_frame, selected_option, *categories, command=show_selection)
dropdown_add.pack(pady=20)

price_add_label = tk.Label(add_frame, text='Item Price', bg='lightgrey', fg='black', font=('Arial', 14))
price_add_label.pack(pady=20)
entry_add_price = tk.Entry(add_frame, width=30, font=('Arial', 14))
entry_add_price.pack(pady=5)

desc_add_label = tk.Label(add_frame, text='Item Description', bg='lightgrey', fg='black', font=('Arial', 14))
desc_add_label.pack(pady=20)
entry_add_desc = tk.Entry(add_frame, width=30, font=('Arial', 14))
entry_add_desc.pack(pady=5)

submit_add_button = tk.Button(add_frame, text="Submit", command=check)
submit_add_button.pack(pady=20)


switch_frame(main_frame)
root.mainloop()
