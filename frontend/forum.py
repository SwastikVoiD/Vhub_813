import customtkinter as ctk
import datetime

def get_timestamp():
    """Generate a formatted timestamp."""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def add_post():
    """Add a new post with a unique key and current timestamp."""
    title = title_entry.get()  # Get the text from the entry field
    if title:  # Check if the title is not empty
        post_id = str(max(map(int, li.keys())) + 1)  # Get the next available key
        li[post_id] = [title, get_timestamp()]  # Add the new post to the dictionary
        update_textbox()  # Update the textbox to display the new post
        title_entry.delete(0, "end")  # Clear the entry field

def update_textbox():
    """Clear and repopulate the textbox with current posts."""
    textbox.delete("1.0", "end")  # Clear existing text
    for post_id, post in li.items():
        title, timestamp = post
        textbox.insert("end", f"{post_id} - {title} - {timestamp}\n\n")

def forum(a):
    global textbox, title_entry, li
    li = {
        "24": ['Post title: asdsa', get_timestamp()],
        "25": ['Post title: sds', get_timestamp()],
    }

    root = ctk.CTk()
    root.title("Forums")
    root.configure(fg_color='white')
    root.geometry("1200x800")

    label = ctk.CTkLabel(root, text="Forum", font=("Comic Sans MS", 40, "bold"), text_color='black')
    label.pack(pady=20)

    textbox = ctk.CTkTextbox(root, width=800, height=600)
    textbox.pack(pady=20)

    # Populate the textbox with initial forum posts
    update_textbox()

    # Entry field for new post title
    title_entry = ctk.CTkEntry(root, placeholder_text="Enter post title")
    title_entry.pack(pady=10)

    # Button to add new post
    add_button = ctk.CTkButton(root, text="Add Post", command=add_post)
    add_button.pack()

    root.mainloop()

