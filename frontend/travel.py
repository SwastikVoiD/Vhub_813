import customtkinter as ctk

def travelpool():
    root = ctk.CTk()
    root.title("Travel Pool")
    root.geometry("800x600")
    root.configure(fg_color='white')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    location_label = ctk.CTkLabel(root, text="Travel Destination", text_color='black', font=('Comic Sans MS', 24))
    location_label.pack(pady=10)
    entry_location = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_location.pack(pady=5)

    date_label = ctk.CTkLabel(root, text="Travel Date (YYYY-MM-DD)", text_color='black', font=('Comic Sans MS', 24))
    date_label.pack(pady=10)
    entry_date = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_date.pack(pady=5)

    time_label = ctk.CTkLabel(root, text="Travel Time (HH:MM)", text_color='black', font=('Comic Sans MS', 24))
    time_label.pack(pady=10)
    entry_time = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_time.pack(pady=5)

    transport_label = ctk.CTkLabel(root, text="Transport Medium (e.g., Car, Bus)", text_color='black', font=('Comic Sans MS', 24))
    transport_label.pack(pady=10)
    entry_transport = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_transport.pack(pady=5)

    people_label = ctk.CTkLabel(root, text="Number of People", text_color='black', font=('Comic Sans MS', 24))
    people_label.pack(pady=10)
    entry_people = ctk.CTkEntry(root, width=300, font=('Comic Sans MS', 14))
    entry_people.pack(pady=5)

    def submit_details():
        destination = entry_location.get()
        date = entry_date.get()
        time = entry_time.get()
        transport = entry_transport.get()
        people = entry_people.get()
        
        details = f"Destination: {destination}\nDate: {date}\nTime: {time}\nTransport: {transport}\nNumber of People: {people}"
        print(details)

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_details)
    submit_button.pack(pady=20)

    root.mainloop()

