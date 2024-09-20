import tkinter as tkr
from tkinter import ttk
from PIL import Image, ImageTk

root = tkr.Tk()
root.title("Login Panel")
root.geometry("570x325")
count = 0

def clear_login():
    txt_User.delete(0, 'end')
    txt_Pass.delete(0, 'end')

def clear_signup():
    txt_User2.delete(0, 'end')
    txt_Pass2.delete(0, 'end')
    txt_name.delete(0, 'end')

def show_login():
    tabControl.select(0)

def show_signup():
    tabControl.select(1)

def logged_in_page():
    global name
    name = txt_User.get()  # For demonstration
    tkr.messagebox.showinfo("Login", f"Welcome {name}!")  # Show welcome message

def showpass():
    global count
    cur = tabControl.index("current")
    count += 1

    if count % 2 == 0:
        char = '•'
        btn_eye['image'] = unhide_icon
    else:
        char = ''
        btn_eye['image'] = hide_icon

    if cur == 0:
        txt_Pass.configure(show=char)
    elif cur == 1:
        txt_Pass2.configure(show=char)

# Set up the main application window and notebook for tabs
tabControl = ttk.Notebook(root, width=631, height=384)
tab1 = tkr.Frame(tabControl)  # Login Tab
tab2 = tkr.Frame(tabControl)  # SignUp Tab

tabControl.add(tab1, text='Login')
tabControl.add(tab2, text='SignUp')
tabControl.grid()

# Canvas for Login Tab
canvas = tkr.Canvas(tab1, width=631, height=384)
canvas.place(relx=.4, rely=.4, anchor='center')
img = ImageTk.PhotoImage(Image.open(r'frontend\\green_3-wallpaper-1366x768.jpg'))
canvas.create_image(20, 20, anchor='nw', image=img)

# Eye icons for password visibility
unhide_icon = ImageTk.PhotoImage(Image.open(r"frontend\\view.png").resize((20, 20), Image.ANTIALIAS))
hide_icon = ImageTk.PhotoImage(Image.open(r"frontend\\hide.png").resize((20, 20), Image.ANTIALIAS))

canvas.create_text(354, 90, fill="white", text="Login Form", font=("Helvetica 19 normal"))
canvas.create_text(225, 162, fill="white", text="Username :", font=("Helvetica 16 normal"))
canvas.create_text(225, 213, fill="white", text="Password :", font=("Helvetica 16 normal"))

# Login Widgets
txt_User = tkr.Entry(tab1, text='', font=("Helvetica 14 normal"))
txt_User.place(relx=.54, rely=.32, anchor='center')
txt_Pass = tkr.Entry(tab1, text='', show='•', font=("Helvetica 14 normal"))
txt_Pass.place(relx=.54, rely=.45, anchor='center')

btn_Login = tkr.Button(tab1, text='Login', font=("Helvetica 13 normal"), width=12, command=logged_in_page)
btn_Login.place(relx=.625, rely=.62, anchor='center')

btn_eye = tkr.Button(tab1, text='', image=unhide_icon, command=showpass, borderwidth=0)
btn_eye.place(relx=.739, rely=.45, anchor='center')

switch_signup = tkr.Button(tab1, text='Don\'t have an account?', font=("Helvetica 13 normal"), width=20, command=show_signup)
switch_signup.place(relx=.34, rely=.62, anchor='center')

# Canvas for SignUp Tab
canvas = tkr.Canvas(tab2, width=631, height=384)
canvas.place(relx=.4, rely=.4, anchor='center')
canvas.create_image(20, 20, anchor='nw', image=img)

canvas.create_text(354, 70, fill="white", text="SignUp Form", font=("Helvetica 19 normal"))
canvas.create_text(225, 138, fill="white", text="Name       :", font=("Helvetica 16 normal"))
canvas.create_text(225, 189, fill="white", text="Username :", font=("Helvetica 16 normal"))
canvas.create_text(225, 240, fill="white", text="Password :", font=("Helvetica 16 normal"))

# SignUp Widgets
txt_name = tkr.Entry(tab2, text='', font=("Helvetica 14 normal"))
txt_name.place(relx=.54, rely=.26, anchor='center')
txt_User2 = tkr.Entry(tab2, text='', font=("Helvetica 14 normal"))
txt_User2.place(relx=.54, rely=.39, anchor='center')
txt_Pass2 = tkr.Entry(tab2, text='', show='•', font=("Helvetica 14 normal"))
txt_Pass2.place(relx=.54, rely=.52, anchor='center')

btn_Signup = tkr.Button(tab2, text='SignUp', font=("Helvetica 13 normal"), width=12, command=clear_signup)
btn_Signup.place(relx=.625, rely=.68, anchor='center')

btn_eye_signup = tkr.Button(tab2, text='', image=unhide_icon, command=showpass, borderwidth=0)
btn_eye_signup.place(relx=.739, rely=.52, anchor='center')

switch_login = tkr.Button(tab2, text='Have an account?', font=("Helvetica 13 normal"), width=20, command=show_login)
switch_login.place(relx=.34, rely=.68, anchor='center')

root.mainloop()
