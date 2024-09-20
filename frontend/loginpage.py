import tkinter as tk
from tkinter import messagebox

def switch_frame(frame):
    frame.tkraise()

def check_password(event=None):  
    print(entry_username.get())
    print(entry_password.get())
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def hidepasswordlogin():
    entry_password.configure(show='*')
    show_password.configure(text='Show Password', command=showpasswordlogin)

def showpasswordlogin():
    entry_password.configure(show='')
    show_password.configure(text='Hide Password', command=hidepasswordlogin)

def hidepasswordcreate():
    entry_create_password.configure(show='*')
    entry_create_confirm_password.configure(show='*')
    show_password.configure(text='Show Password', command=showpasswordcreate)

def showpasswordcreate():
    entry_create_password.configure(show='')
    entry_create_confirm_password.configure(show='')
    show_password.configure(text='Hide Password', command=hidepasswordcreate)

def showpasswordcreateconfirm():
    entry_create_confirm_password.configure(show='')
    show_password.configure(text='Hide Password', command=hidepasswordcreateconfirm)

def hidepasswordcreateconfirm():
    entry_create_confirm_password.configure(show='')
    show_password.configure(text='Hide Password', command=showpasswordcreateconfirm)

def createaccount():
    user=entry_create_username.get()
    password=entry_create_password.get()
    password_confirm=entry_create_confirm_password.get()
    if password!=password_confirm:
        a = messagebox.showinfo('Error', 'Password not matching')
        print(a)
        entry_create_password.delete(0,tk.END)
        entry_create_confirm_password.delete(0,tk.END)


root = tk.Tk()
root.title('Authentication Page')
root.geometry("800x600")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

login_frame = tk.Frame(root, bg='lightgrey')
create_account_frame = tk.Frame(root, bg='lightgrey')

for frame in (login_frame, create_account_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Login Frame
main_label=tk.Label(login_frame,text='LOGIN PAGE',bg='lightgrey',fg='black',font=('ALGERIAN',20))
main_label.pack(pady=30)

username_label = tk.Label(login_frame, text='Enter Username', bg='lightgrey',fg='black', font=('Arial', 14))
username_label.pack(pady=20)
entry_username = tk.Entry(login_frame, width=30, font=('Arial', 14))
entry_username.pack(pady=5)

password_label = tk.Label(login_frame, text='Enter Password', bg='lightgrey',fg='black', font=('Arial', 14))
password_label.pack(pady=20)
entry_password = tk.Entry(login_frame, show="*", width=30, font=('Arial', 14))
entry_password.pack(pady=5)

show_password = tk.Button(login_frame, text="Show Password", command=showpasswordlogin, fg='black')
show_password.place(x=570,y=275)

submit_button=tk.Button(login_frame,text="Login",command=check_password,fg='black')
submit_button.place(x=300,y=320)

create_account_option_button = tk.Button(login_frame, text="Don't have an account? Create an account", command=lambda: switch_frame(create_account_frame), fg='black')
create_account_option_button.place(x=400,y=320)

# Create Account Frame
main_create_label=tk.Label(create_account_frame,text='CREATE ACCOUNT',bg='lightgrey',fg='black',font=('ALGERIAN',20))
main_create_label.pack(pady=30)

username_create_label = tk.Label(create_account_frame, text='Create Username', bg='lightgrey', fg='black', font=('Arial', 14))
username_create_label.pack(pady=20)
extra_label=tk.Label(create_account_frame,text="Username for Students is Your Registeration Number ex. 24BMEXXXX")
extra_label.pack()
entry_create_username = tk.Entry(create_account_frame, width=30, font=('Arial', 14))
entry_create_username.pack(pady=5)

password_create_label = tk.Label(create_account_frame, text='Create Password', bg='lightgrey', fg='black', font=('Arial', 14))
password_create_label.pack(pady=20)
entry_create_password = tk.Entry(create_account_frame, show="*", width=30, font=('Arial', 14))
entry_create_password.pack(pady=5)

confirm_password_create_label = tk.Label(create_account_frame, text='Confirm Password', bg='lightgrey', fg='black', font=('Arial', 14))
confirm_password_create_label.pack(pady=20)
entry_create_confirm_password = tk.Entry(create_account_frame, show="*", width=30, font=('Arial', 14))
entry_create_confirm_password.pack(pady=5)

show_create_password = tk.Button(create_account_frame, text="Show Password", command=showpasswordcreate, fg='black')
show_create_password.place(x=570,y=295)

show_create_password = tk.Button(create_account_frame, text="Show Password", command=showpasswordcreateconfirm, fg='black')
show_create_password.place(x=570,y=400)

submit_create_button = tk.Button(create_account_frame, text='Create Account', command=createaccount)
submit_create_button.place(x=250,y=440)

login_option_button = tk.Button(create_account_frame, text='Already have an account? Login', command=lambda: switch_frame(login_frame),fg='black')
login_option_button.place(x=400,y=440)

switch_frame(login_frame)
root.mainloop()
