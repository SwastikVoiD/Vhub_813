import customtkinter as ctk
import sql_commands
import datetime


def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def add_post(user):
    content = content_entry.get() 
    if content: 
        sql_commands.forum_add(user,content)
        update_textbox()  
        content_entry.delete(0, "end")

def update_textbox():
    textbox.delete("1.0", "end")  
    result=sql_commands.forum_update()
    for post in result:
        user, content, timestamp = post
        textbox.insert("end", f"{user} - {content} - {timestamp}\n\n")

def forum(regno):
    global textbox, content_entry

    root = ctk.CTk()
    root.title("Forums")
    root.state('normal')
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.configure(fg_color='black')
    
    label = ctk.CTkLabel(root, text="Forum", font=("Comic Sans MS", 40, "bold"), text_color='white')
    label.pack(pady=20)

    textbox = ctk.CTkTextbox(root, width=800, height=600)
    textbox.place(x=50, y=150)

    update_textbox()

    content_entry = ctk.CTkEntry(root, placeholder_text="Enter post content", width=250)
    content_entry.place(x=900, y=150)

    add_button = ctk.CTkButton(root, text="Add Post", command=lambda: add_post(regno))
    add_button.place(x=900, y=190)

    ctk.CTkButton(root,text="Back",command=root.destroy).place(x=10,y=10)
    root.mainloop()



