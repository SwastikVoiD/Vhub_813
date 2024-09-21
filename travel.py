import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

# MySQL database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  # your MySQL username
    'password': 'abc+1234',  # your MySQL password
    'database': 'vhub'  # your database name
}

# Connect to the database
try:
    db_connection = mysql.connector.connect(**DB_CONFIG)
    cursor = db_connection.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")

def travelpool():
    root = ctk.CTk()
    root.title("Travel Pool")
    root.geometry("800x600")
    root.configure(fg_color='white')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(root, text="Travel Destination", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_location = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_location.pack(pady=5)

    ctk.CTkLabel(root, text="Travel Date (YYYY-MM-DD)", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_date = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_date.pack(pady=5)

    ctk.CTkLabel(root, text="Travel Time (HH:MM)", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_time = ctk.CTkEntry(root, width=300, font=('Arial', 14))
    entry_time.pack(pady=5)

    ctk.CTkLabel(root, text="Transport Medium (e.g., Car, Bus)", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_transport = ctk.CTkEntry(root, width=300, font=('Arial', 14))
    entry_transport.pack(pady=5)

    ctk.CTkLabel(root, text="Number of People", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_people = ctk.CTkEntry(root, width=300, font=('Arial', 14))
    entry_people.pack(pady=5)

    def submit_details():
        destination = entry_location.get()
        date = entry_date.get()
        time = entry_time.get()
        transport = entry_transport.get()
        people = entry_people.get()

        # Validate inputs
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
            if not people.isdigit():
                raise ValueError("Number of people must be a digit.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Insert details into the database
        query = "INSERT INTO travel_details (destination, travel_date, travel_time, transport, number_of_people) VALUES (%s, %s, %s, %s, %s)"
        values = (destination, date, time, transport, int(people))
        
        try:
            cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Success", "Travel details submitted successfully!")
            # Clear the fields
            entry_location.delete(0, 'end')
            entry_date.delete(0, 'end')
            entry_time.delete(0, 'end')
            entry_transport.delete(0, 'end')
            entry_people.delete(0, 'end')
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to insert details: {err}")

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_details)
    submit_button.pack(pady=20)

    root.mainloop()

