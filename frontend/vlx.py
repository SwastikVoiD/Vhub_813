import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

def vlx():
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

    root = ctk.CTk()
    root.configure(fg_color='lightgrey')
    root.geometry("1200x800")
    root.title('VLX')

    main_frame = ctk.CTkFrame(root, fg_color='lightgrey')
    search_frame = ctk.CTkFrame(root, fg_color='lightgrey')
    add_frame = ctk.CTkFrame(root, fg_color='lightgrey')

    for frame in (search_frame, add_frame, main_frame):
        frame.grid(row=0, column=0, sticky="nsew")

    # Initialize global variable
    global categories_selected
    categories_selected = "Choose Category"
    selected_option = ctk.StringVar(value=categories_selected)
    categories = ["Electronics", "Stationary", "Sports", "Fashion", "Foods and Beverages"]

    # Add Item Frame
    item_add_label = ctk.CTkLabel(add_frame, text='Item Name', text_color='black', font=('Arial', 14))
    item_add_label.pack(pady=10)
    entry_add_item = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_item.pack(pady=5)

    categories_add_label = ctk.CTkLabel(add_frame, text='Item Category', text_color='black', font=('Arial', 14))
    categories_add_label.pack(pady=10)
    dropdown_add = ctk.CTkOptionMenu(add_frame, selected_option, *categories, command=show_selection)
    dropdown_add.pack(pady=5)

    price_add_label = ctk.CTkLabel(add_frame, text='Item Price', text_color='black', font=('Arial', 14))
    price_add_label.pack(pady=10)
    entry_add_price = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_price.pack(pady=5)

    desc_add_label = ctk.CTkLabel(add_frame, text='Item Description', text_color='black', font=('Arial', 14))
    desc_add_label.pack(pady=10)
    entry_add_desc = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_desc.pack(pady=5)

    submit_add_button = ctk.CTkButton(add_frame, text="Submit", command=submitadd)
    submit_add_button.pack(pady=10)

    back_button_add = ctk.CTkButton(add_frame, text="Back", command=lambda: switch_frame(main_frame))
    back_button_add.pack(pady=10)

    # Search Item Frame
    item_search_label = ctk.CTkLabel(search_frame, text="Enter Item Name", text_color='black', font=('Arial', 14))
    item_search_label.pack(pady=10)
    entry_search_item = ctk.CTkEntry(search_frame, width=300, font=("Arial", 14))
    entry_search_item.pack(pady=5)

    categories_search_label = ctk.CTkLabel(search_frame, text='Item Category', text_color='black', font=('Arial', 14))
    categories_search_label.pack(pady=10)
    dropdown_search = ctk.CTkOptionMenu(search_frame, selected_option, *categories, command=show_selection)
    dropdown_search.pack(pady=5)

    submit_search_button = ctk.CTkButton(search_frame, text="Submit", command=submitsearch)
    submit_search_button.pack(pady=10)

    back_button_search = ctk.CTkButton(search_frame, text="Back", command=lambda: switch_frame(main_frame))
    back_button_search.pack(pady=10)

    # Main Frame
    main_label = ctk.CTkLabel(main_frame, text="WELCOME TO VLX", text_color='black', font=('Arial', 24))
    main_label.pack(pady=20)

    add_button = ctk.CTkButton(main_frame, text="Add Item", command=lambda: switch_frame(add_frame))
    add_button.pack(pady=10)

    search_button = ctk.CTkButton(main_frame, text="Search Item", command=lambda: switch_frame(search_frame))
    search_button.pack(pady=10)

    switch_frame(main_frame)
    root.mainloop()

# Call the vlx function to run the application
vlx()
