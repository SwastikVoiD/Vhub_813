import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import homepage
import sql_commands

def switch_frame(frame):
    frame.tkraise()

def check_password(event=None):
    user = entry_username.get()
    pwd = entry_password.get()
    email=sql_commands.getname(user,pwd)
    if sql_commands.login(user,pwd):
        try:
            homepage.homepage(user,email)  
            entry_username.delete(0, ctk.END)
            entry_password.delete(0, ctk.END)
            root.after(100, root.destroy)
        except Exception as e:
            print(f"Error during homepage switch: {e}")
    else:
        messagebox.showinfo('Error', 'Passwords do not match')
        entry_username.delete(0, ctk.END)
        entry_password.delete(0, ctk.END)

def toggle_password(entry, button, is_visible):
    if is_visible:
        entry.configure(show='*')
        button.configure(image=unhide_icon)  # Closed eye icon
    else:
        entry.configure(show='')
        button.configure(image=hide_icon)  # Open eye icon
    return not is_visible

def createaccount():
    user = entry_create_username.get()
    password = entry_create_password.get()
    password_confirm = entry_create_confirm_password.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    gender = entry_gender.get()
    phone = entry_phone.get()
    email = entry_email.get()
    hostel = entry_hostel.get()
    room_no = entry_room_no.get()
    emergency_phone = entry_emergency_phone.get()
    
    if password != password_confirm:
        messagebox.showinfo('Error', 'Passwords do not match')
        entry_create_password.delete(0, ctk.END)
        entry_create_confirm_password.delete(0, ctk.END)
    else:
        sql_commands.new_user(user,password,first_name,last_name,dob,gender,hostel,room_no,phone,emergency_phone,email)
        messagebox.showinfo('Success','Account created successfully.')
        switch_frame(login_frame)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title('Authentication Page')
root.geometry("1200x800")
root.configure(bg='lightgrey')
root.attributes('-fullscreen',True)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

unhide_icon = Image.open("view.png").resize((20, 20), Image.LANCZOS)
unhide_icon = ctk.CTkImage(unhide_icon)

hide_icon = Image.open("hide.png").resize((20, 20), Image.LANCZOS)
hide_icon = ctk.CTkImage(hide_icon)

# Frames
login_frame = ctk.CTkFrame(root, fg_color='lightgrey')
create_account_frame = ctk.CTkFrame(root, fg_color='lightgrey')
page2_frame = ctk.CTkFrame(root, fg_color='lightgrey')
page3_frame = ctk.CTkFrame(root, fg_color='lightgrey')

for frame in (login_frame, create_account_frame, page2_frame, page3_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Login Frame
main_label = ctk.CTkLabel(login_frame, text='LOGIN PAGE', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 24))
main_label.pack(pady=30)

username_label = ctk.CTkLabel(login_frame, text='Enter Username', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
username_label.pack(pady=20)
entry_username = ctk.CTkEntry(login_frame, width=300, font=('Comic Sans MS', 14))
entry_username.pack(pady=5)

password_label = ctk.CTkLabel(login_frame, text='Enter Password', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
password_label.pack(pady=20)
entry_password = ctk.CTkEntry(login_frame, show="*", width=300, font=('Comic Sans MS', 14))
entry_password.pack(pady=5)

# Toggle password visibility
show_password_button = ctk.CTkButton(login_frame, text='', image=unhide_icon, 
                                       command=lambda: toggle_password(entry_password, show_password_button, entry_password.cget('show') == ''), 
                                       width=30, height=30, border_width=0)
show_password_button.place(x=775, y=270)

submit_button = ctk.CTkButton(login_frame, text="Login", command=check_password, fg_color='black', font=('Comic Sans MS', 14), width=20, height=2, border_width=0)
submit_button.pack(pady=20)

create_account_option_button = ctk.CTkButton(login_frame, text="Don't have an account? Create an account", 
                                               command=lambda: switch_frame(create_account_frame), 
                                               fg_color='black', font=('Comic Sans MS', 14), width=40, height=2, border_width=0)
create_account_option_button.pack(pady=10)

# Create Account Frame
main_create_label = ctk.CTkLabel(create_account_frame, text='CREATE ACCOUNT', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 24))
main_create_label.pack(pady=30)

username_create_label = ctk.CTkLabel(create_account_frame, text='Create Username', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
username_create_label.pack(pady=20)
entry_create_username = ctk.CTkEntry(create_account_frame, width=300, font=('Comic Sans MS', 14), placeholder_text="Registration Number ex. 24BMEXXXX")
entry_create_username.pack(pady=5)

password_create_label = ctk.CTkLabel(create_account_frame, text='Create Password', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
password_create_label.pack(pady=20)
entry_create_password = ctk.CTkEntry(create_account_frame, show="*", width=300, font=('Comic Sans MS', 14))
entry_create_password.pack(pady=5)

# Toggle password visibility for create account
show_create_password_button = ctk.CTkButton(create_account_frame, text='', image=hide_icon, 
                                              command=lambda: toggle_password(entry_create_password, show_create_password_button, entry_create_password.cget('show') == ''), 
                                              width=30, height=30, border_width=0)
show_create_password_button.place(x=775, y=270)

confirm_password_create_label = ctk.CTkLabel(create_account_frame, text='Confirm Password', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
confirm_password_create_label.pack(pady=20)
entry_create_confirm_password = ctk.CTkEntry(create_account_frame, show="*", width=300, font=('Comic Sans MS', 14))
entry_create_confirm_password.pack(pady=5)

# Toggle password visibility for confirm password
show_create_confirm_password_button = ctk.CTkButton(create_account_frame, text='', image=hide_icon, 
                                                      command=lambda: toggle_password(entry_create_confirm_password, show_create_confirm_password_button, entry_create_confirm_password.cget('show') == ''), 
                                                      width=30, height=30, border_width=0)
show_create_confirm_password_button.place(x=775, y=375)

nextpage_create_button = ctk.CTkButton(create_account_frame, text='Next Page',width=20, height=2, border_width=0, font=('Comic Sans MS', 14),command=lambda:switch_frame(page2_frame))
nextpage_create_button.pack(pady=20)

login_option_button = ctk.CTkButton(create_account_frame, text='Already have an account? Login', 
                                      command=lambda: switch_frame(login_frame), 
                                      fg_color='black', width=40, height=2, border_width=0, font=('Comic Sans MS', 14))
login_option_button.pack(pady=10)

# Page 2 Frame (User Details)
main_page2_label = ctk.CTkLabel(page2_frame, text='USER DETAILS', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 24))
main_page2_label.pack(pady=30)

first_name_label = ctk.CTkLabel(page2_frame, text='First Name', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
first_name_label.pack(pady=10)
entry_first_name = ctk.CTkEntry(page2_frame, width=300, font=('Comic Sans MS', 14))
entry_first_name.pack(pady=5)

last_name_label = ctk.CTkLabel(page2_frame, text='Last Name', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
last_name_label.pack(pady=10)
entry_last_name = ctk.CTkEntry(page2_frame, width=300, font=('Comic Sans MS', 14))
entry_last_name.pack(pady=5)

dob_label = ctk.CTkLabel(page2_frame, text='Date of Birth (YYYY-MM-DD)', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
dob_label.pack(pady=10)
entry_dob = ctk.CTkEntry(page2_frame, width=300, font=('Comic Sans MS', 14))
entry_dob.pack(pady=5)

gender_label = ctk.CTkLabel(page2_frame, text='Gender', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
gender_label.pack(pady=10)
entry_gender = ctk.CTkEntry(page2_frame, width=300, font=('Comic Sans MS', 14))
entry_gender.pack(pady=5)

phone_label = ctk.CTkLabel(page2_frame, text='Phone Number', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
phone_label.pack(pady=10)
entry_phone = ctk.CTkEntry(page2_frame, width=300, font=('Comic Sans MS', 14))
entry_phone.pack(pady=5)

email_label = ctk.CTkLabel(page2_frame, text='Email ID', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
email_label.pack(pady=10)
entry_email = ctk.CTkEntry(page2_frame, width=300, font=('Comic Sans MS', 14))
entry_email.pack(pady=5)

# Back button to return to the Create Account frame
back_button = ctk.CTkButton(page2_frame, text='Back', command=lambda: switch_frame(create_account_frame), width=20, height=2, border_width=0, font=('Comic Sans MS', 14))
back_button.pack(pady=20)

submit_page2_button = ctk.CTkButton(page2_frame, text='Next Page', command=lambda: switch_frame(page3_frame), width=20, height=2, border_width=0, font=('Comic Sans MS', 14))
submit_page2_button.pack()

# Page 3 Frame (Hostel Information)
main_page3_label = ctk.CTkLabel(page3_frame, text='HOSTEL DETAILS', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 24))
main_page3_label.pack(pady=30)

hostel_label = ctk.CTkLabel(page3_frame, text='Hostel', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
hostel_label.pack(pady=10)
entry_hostel = ctk.CTkEntry(page3_frame, width=300, font=('Comic Sans MS', 14))
entry_hostel.pack(pady=5)

room_no_label = ctk.CTkLabel(page3_frame, text='Room Number', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
room_no_label.pack(pady=10)
entry_room_no = ctk.CTkEntry(page3_frame, width=300, font=('Comic Sans MS', 14))
entry_room_no.pack(pady=5)

emergency_phone_label = ctk.CTkLabel(page3_frame, text='Emergency Phone Number', fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 14))
emergency_phone_label.pack(pady=10)
entry_emergency_phone = ctk.CTkEntry(page3_frame, width=300, font=('Comic Sans MS', 14))
entry_emergency_phone.pack(pady=5)

submit_page3_button = ctk.CTkButton(page3_frame, text='Submit Details', command=createaccount, width=20, height=2, border_width=0, font=('Comic Sans MS', 14))
submit_page3_button.pack(pady=20)

back_to_page2_button = ctk.CTkButton(page3_frame, text='Back', command=lambda: switch_frame(page2_frame), width=20, height=2, border_width=0, font=('Comic Sans MS', 14))
back_to_page2_button.pack(pady=10)

# Start with the login frame
switch_frame(login_frame)
root.mainloop()
