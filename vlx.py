import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

def vlx():
    # Establish MySQL connection
    db_config = {
        'user': 'your_username',       # Replace with your MySQL username
        'password': 'your_password',   # Replace with your MySQL password
        'host': 'localhost',
        'database': 'vlx_db'
    }
    
    try:
        db_connection = mysql.connector.connect(**db_config)
        cursor = db_connection.cursor()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return

    def switch_frame(frame):
        frame.tkraise()
        # Reset category selection on frame switch
        selected_category.set(None)

    def toggle_category(category):
        # Set the selected category
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
        
        # Insert item into database
        insert_query = "INSERT INTO items (item_name, category, price, description, timestamp) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (item, selected, float(price), desc, timestamp))
        db_connection.commit()
        messagebox.showinfo("Success", "Item added successfully!")
        entry_add_item.delete(0, ctk.END)
        entry_add_price.delete(0, ctk.END)
        entry_add_desc.delete(0, ctk.END)

    def submitsearch():
        item = entry_search_item.get()
        selected = selected_category.get()
        
        search_query = "SELECT * FROM items WHERE item_name LIKE %s AND category = %s"
        cursor.execute(search_query, (f"%{item}%", selected))
        results = cursor.fetchall()

        if results:
            for row in results:
                print(row)  # You can display this in a more user-friendly way if needed
        else:
            messagebox.showinfo("Search Result", "No items found.")

    # Create main window
    root = ctk.CTk()
    root.configure(fg_color='lightgrey')
    root.geometry("1200x800")
    root.title('VLX')

    # Create frames
    main_frame = ctk.CTkFrame(root, fg_color='lightgrey')
    search_frame = ctk.CTkFrame(root, fg_color='lightgrey')
    add_frame = ctk.CTkFrame(root, fg_color='lightgrey')

    for frame in (main_frame, search_frame, add_frame):
        frame.grid(row=0, column=0, sticky="nsew")

    # Categories
    categories = ["Electronics", "Stationary", "Sports", "Fashion", "Foods and Beverages"]
    selected_category = ctk.StringVar(value=None)

    # Add Item Frame
    ctk.CTkLabel(add_frame, text='Item Name', text_color='black', font=('Arial', 14)).pack(pady=10)
    entry_add_item = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_item.pack(pady=5)

    ctk.CTkLabel(add_frame, text='Item Category', text_color='black', font=('Arial', 14)).pack(pady=10)
    for category in categories:
        checkbox = ctk.CTkCheckBox(
            add_frame, 
            text=category, 
            variable=selected_category, 
            onvalue=category, 
            offvalue=None, 
            command=lambda cat=category: toggle_category(cat)
        )
        checkbox.pack(anchor='w')
        checkbox.configure(text_color='black')

    ctk.CTkLabel(add_frame, text='Item Price', text_color='black', font=('Arial', 14)).pack(pady=10)
    entry_add_price = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_price.pack(pady=5)

    ctk.CTkLabel(add_frame, text='Item Description', text_color='black', font=('Arial', 14)).pack(pady=10)
    entry_add_desc = ctk.CTkEntry(add_frame, width=300, font=('Arial', 14))
    entry_add_desc.pack(pady=5)

    ctk.CTkButton(add_frame, text="Submit", command=submitadd).pack(pady=10)
    ctk.CTkButton(add_frame, text="Back", command=lambda: switch_frame(main_frame)).pack(pady=10)

    # Search Item Frame
    ctk.CTkLabel(search_frame, text="Enter Item Name", text_color='black', font=('Arial', 14)).pack(pady=10)
    entry_search_item = ctk.CTkEntry(search_frame, width=300, font=("Arial", 14))
    entry_search_item.pack(pady=5)

    ctk.CTkLabel(search_frame, text='Item Category', text_color='black', font=('Arial', 14)).pack(pady=10)
    for category in categories:
        checkbox = ctk.CTkCheckBox(
            search_frame, 
            text=category, 
            variable=selected_category, 
            onvalue=category, 
            offvalue=None, 
            command=lambda cat=category: toggle_category(cat)
        )
        checkbox.pack(anchor='w')
        checkbox.configure(text_color='black')

    ctk.CTkButton(search_frame, text="Submit", command=submitsearch).pack(pady=10)
    ctk.CTkButton(search_frame, text="Back", command=lambda: switch_frame(main_frame)).pack(pady=10)

    # Main Frame
    ctk.CTkLabel(main_frame, text="WELCOME TO VLX", text_color='black', font=('Arial', 24)).pack(pady=20)
    ctk.CTkButton(main_frame, text="Add Item", command=lambda: switch_frame(add_frame)).pack(pady=10)
    ctk.CTkButton(main_frame, text="Search Item", command=lambda: switch_frame(search_frame)).pack(pady=10)

    # Start in the main frame
    switch_frame(main_frame)

    # Run the application
    root.mainloop()

    # Close database connection on exit
    cursor.close()
    db_connection.close()
