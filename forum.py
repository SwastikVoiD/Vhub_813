import customtkinter as ctk
import mysql.connector
import datetime

# Database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'abc+1234',
    'database': 'vhub'
}

def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def add_post(user):
    content = content_entry.get()  # from the entry field
    if content:  # Check if the content is not empty
        # Insert the new post into the database
        cursor.execute("INSERT INTO forum (user, content) VALUES (%s, %s)", (user, content))
        db_connection.commit()  # Commit the transaction
        update_textbox()  # Update the textbox to display the new post
        content_entry.delete(0, "end")  # Clear the entry field

def update_textbox():
    textbox.delete("1.0", "end")  # Clear existing text
    cursor.execute("SELECT user, content, timestamp FROM forum")  # Fetch all forum posts
    for post in cursor.fetchall():
        user, content, timestamp = post
        textbox.insert("end", f"{user} - {content} - {timestamp}\n\n")

def forum(regno):
    global textbox, content_entry, db_connection, cursor

    # Establish database connection
    db_connection = mysql.connector.connect(**DB_CONFIG)
    cursor = db_connection.cursor()

    root = ctk.CTk()
    root.title("Forums")
    root.configure(fg_color='white')
    root.geometry("1200x800")
    root.state('zoomed')

    label = ctk.CTkLabel(root, text="Forum", font=("Comic Sans MS", 40, "bold"), text_color='black')
    label.pack(pady=20)

    textbox = ctk.CTkTextbox(root, width=800, height=600)
    textbox.place(x=50, y=150)

    # Populate the textbox with initial forum posts
    update_textbox()

    # Entry field for new post content
    content_entry = ctk.CTkEntry(root, placeholder_text="Enter post content", width=250)
    content_entry.place(x=900, y=150)

    # Button to add new post
    add_button = ctk.CTkButton(root, text="Add Post", command=lambda: add_post(regno))
    add_button.place(x=900, y=190)

    root.mainloop()

    # Close database connection on exit
    cursor.close()
    db_connection.close()

