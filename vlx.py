import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import sql_commands

def vlx():
    def switch_frame(frame):
        frame.tkraise()
        selected_category.set(None)  # Reset category selection

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

    # Create main window
    root = ctk.CTk()
    root.configure(fg_color='white')
    root.geometry("1200x800")
    root.attributes('-fullscreen', True)
    root.title('VLX')

    # Create frames
    search_frame = ctk.CTkFrame(root, fg_color='lightgrey')
    add_frame = ctk.CTkFrame(root, fg_color='lightgrey')

    # Place frames in grid
    search_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
    add_frame.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')

    # Categories
    categories = ["Electronics", "Stationary", "Sports", "Fashion", "Foods and Beverages"]
    selected_category = ctk.StringVar(value=None)

    # Add Item Frame
    ctk.CTkLabel(add_frame,text="Add Item",text_color='black',font=('Comic Sans MS',17,'bold')).grid(pady=10)
    ctk.CTkLabel(add_frame, text='Item Name', text_color='black', font=('Arial', 14)).grid(pady=10)
    entry_add_item = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_item.grid(pady=5,padx=15)

    ctk.CTkLabel(add_frame, text='Item Category', text_color='black', font=('Arial', 14)).grid(pady=10)
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
        checkbox.configure(text_color='black')

    ctk.CTkLabel(add_frame, text='Item Price', text_color='black', font=('Arial', 14)).grid(pady=10)
    entry_add_price = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_price.grid(pady=5,padx=15)

    ctk.CTkLabel(add_frame, text='Item Description', text_color='black', font=('Arial', 14)).grid(pady=10)
    entry_add_desc = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_desc.grid(pady=5,padx=15)

    ctk.CTkButton(add_frame, text="Submit", command=submitadd).grid(pady=10)
    ctk.CTkButton(add_frame, text="Back", command=lambda: switch_frame(root)).grid(pady=10)

    # Search Item Frame
    ctk.CTkLabel(search_frame,text="Search Item",text_color='black',font=('Comic Sans MS',17,'bold')).grid(pady=10)
    ctk.CTkLabel(search_frame, text="Item Name", text_color='black', font=('Arial', 14)).grid(pady=10)
    entry_search_item = ctk.CTkEntry(search_frame, width=300, font=("Arial", 14))
    entry_search_item.grid(pady=5,padx=15)

    ctk.CTkLabel(search_frame, text='Item Category', text_color='black', font=('Arial', 14)).grid(pady=10)
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
        checkbox.configure(text_color='black')

    ctk.CTkButton(search_frame, text="Submit", command=submitsearch).grid(pady=10)
    ctk.CTkButton(search_frame, text="Back", command=lambda: switch_frame(root)).grid(pady=10)

    # Main label
    main_label = ctk.CTkLabel(root, text="WELCOME TO VLX", text_color='black', font=('Algerian', 30))
    main_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Main frame configuration
    root.grid_rowconfigure(1, weight=1)  # Allow row 1 to expand
    root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
    root.grid_columnconfigure(1, weight=1)  # Allow column 1 to expand

    # Run the application
    root.mainloop()

vlx()
