import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import sql_commands

def vlx():
    def switch_frame(frame):
        frame.tkraise()
        selected_category.set(None)

    def toggle_category(category):
        selected_category.set(category)

    def submitadd():
        item = entry_add_item.get()
        price = entry_add_price.get()
        desc = entry_add_desc.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selected = selected_category.get()

        if not item or not price or not desc or selected is None:
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        
        if not price.isdigit():
            messagebox.showerror("Error", "Invalid price. Please enter a numeric value.")
            return
        
        sql_commands.vlx_sql_submitadd(item, selected, price, desc, timestamp)
        messagebox.showinfo("Success", "Item added successfully!")
        entry_add_item.delete(0, ctk.END)
        entry_add_price.delete(0, ctk.END)
        entry_add_desc.delete(0, ctk.END)

    def submitsearch():
        item = entry_search_item.get()
        selected = selected_category.get()
        
        results = sql_commands.vlx_sql_submitsearch(item, selected)

        if results:
            for row in results:
                messagebox.showinfo("Item Found", f"Item Name: {row[0]}, Category: {row[1]}, Price: {row[2]}, Description: {row[3]}")
        else:
            messagebox.showinfo("Search Result", "No items found.")

    root = ctk.CTk()
    root.state('normal')
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.configure(fg_color='black')
    root.title('VLX')

    search_frame = ctk.CTkFrame(root, fg_color='black')
    add_frame = ctk.CTkFrame(root, fg_color='black')

    search_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
    add_frame.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')

    categories = ["Electronics", "Stationary", "Sports", "Fashion", "Foods and Beverages"]
    selected_category = ctk.StringVar(value=None)

    ctk.CTkLabel(add_frame, text="Add Item", text_color='white', font=('Comic Sans MS', 17, 'bold')).grid(pady=10)
    ctk.CTkLabel(add_frame, text='Item Name', text_color='white', font=('Arial', 14)).grid(pady=10)
    entry_add_item = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_item.grid(pady=5, padx=15)

    ctk.CTkLabel(add_frame, text='Item Category', text_color='white', font=('Arial', 14)).grid(pady=10)
    for category in categories:
        checkbox = ctk.CTkCheckBox(
            add_frame, 
            text=category, 
            variable=selected_category, 
            onvalue=category, 
            offvalue=None, 
            command=lambda cat=category: toggle_category(cat)
        )
        checkbox.grid(sticky='w')
        checkbox.configure(text_color='white')

    ctk.CTkLabel(add_frame, text='Item Price', text_color='white', font=('Arial', 14)).grid(pady=10)
    entry_add_price = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_price.grid(pady=5, padx=15)

    ctk.CTkLabel(add_frame, text='Item Description', text_color='white', font=('Arial', 14)).grid(pady=10)
    entry_add_desc = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_desc.grid(pady=5, padx=15)

    ctk.CTkButton(add_frame, text="Submit", command=submitadd).grid(pady=10)

    ctk.CTkLabel(search_frame, text="Search Item", text_color='white', font=('Comic Sans MS', 17, 'bold')).grid(pady=10)
    ctk.CTkLabel(search_frame, text="Item Name", text_color='white', font=('Arial', 14)).grid(pady=10)
    entry_search_item = ctk.CTkEntry(search_frame, width=300, font=("Arial", 14))
    entry_search_item.grid(pady=5, padx=15)

    ctk.CTkLabel(search_frame, text='Item Category', text_color='white', font=('Arial', 14)).grid(pady=10)
    for category in categories:
        checkbox = ctk.CTkCheckBox(
            search_frame, 
            text=category, 
            variable=selected_category, 
            onvalue=category, 
            offvalue=None, 
            command=lambda cat=category: toggle_category(cat)
        )
        checkbox.grid(sticky='w')
        checkbox.configure(text_color='white')

    ctk.CTkButton(search_frame, text="Submit", command=submitsearch).grid(pady=10)

    ctk.CTkLabel(root, text="WELCOME TO VLX", text_color='white', font=('Algerian', 30)).grid(row=0, column=0, columnspan=2, pady=20)
    ctk.CTkButton(root, text="Back", command=root.destroy).place(x=10,y=10)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()
