import customtkinter as ctk
from tkinter import messagebox, Toplevel
from datetime import datetime
import sql_commands
from tkcalendar import Calendar
def travelpool():
    root = ctk.CTk()
    root.title("Travel Pool")
    root.geometry("800x600")
    root.attributes('-fullscreen',True)

    root.configure(fg_color='white')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Travel Destination
    ctk.CTkLabel(root, text="Travel Destination", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_location = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_location.pack(pady=5)

    # Travel Date
    ctk.CTkLabel(root, text="Travel Date", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    calendar = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.pack(pady=5)

    # Travel Time
    ctk.CTkLabel(root, text="Travel Time (HH:MM)", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_time = ctk.CTkEntry(root, width=300, font=('Arial', 14))
    entry_time.pack(pady=5)

    # Transport Medium
    ctk.CTkLabel(root, text="Transport Medium (e.g., Car, Bus)", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_transport = ctk.CTkEntry(root, width=300, font=('Arial', 14))
    entry_transport.pack(pady=5)

    # Number of People
    ctk.CTkLabel(root, text="Number of People", text_color='black', font=('Comic Sans MS', 24)).pack(pady=10)
    entry_people = ctk.CTkEntry(root, width=300, font=('Arial', 14))
    entry_people.pack(pady=5)

    def submit_details():
        destination = entry_location.get()
        date = calendar.get_date()
        time = entry_time.get()
        transport = entry_transport.get()
        people = entry_people.get()

        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
            if not people.isdigit():
                raise ValueError("Number of people must be a digit.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        try:
            if sql_commands.travel_submit(destination,date,time,transport,people):
                messagebox.showinfo("Success", "Travel details submitted successfully!")
            entry_location.delete(0, 'end')
            entry_time.delete(0, 'end')
            entry_transport.delete(0, 'end')
            entry_people.delete(0, 'end')
        except Exception as err:
            messagebox.showerror("Error", f"{err}")

    def check_details():
        destination = entry_location.get()
        date = calendar.get_date()

        # Validate inputs
        if not destination or not date:
            messagebox.showerror("Error", "Destination and Date must be filled to check for existing details.")
            return

        try:
            results=sql_commands.travel_check(destination,date)            
            if results:
                show_existing_entries(results)
            else:
                messagebox.showinfo("Existing Details", "No existing entries found for this travel plan.")
        except Exception as err:
            messagebox.showerror("Error", f"{err}")

    def show_existing_entries(entries):
        """Show a new window with the existing entries."""
        top = Toplevel(root)
        top.title("Existing Travel Entries")
        top.geometry("400x300")

        listbox = ctk.CTkTextbox(top)
        listbox.pack(pady=10, fill='both', expand=True)

        for entry in entries:
            listbox.insert('end', f"Destination: {entry[1]}, Date: {entry[2]}, Time: {entry[3]}, Transport: {entry[4]}, People: {entry[5]}\n")

        ctk.CTkButton(top, text="Close", command=top.destroy).pack(pady=10)

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_details)
    submit_button.pack(pady=20)

    check_button = ctk.CTkButton(root, text="Check Existing Details", command=check_details)
    check_button.pack(pady=10)

    ctk.CTkButton(root,text="Back",command=root.destroy).place(x=10,y=10)

    root.mainloop()
