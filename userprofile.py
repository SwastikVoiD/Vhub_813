import customtkinter as ctk
import sql_commands
from CustomTkinterMessagebox import CTkMessagebox


def checkpassword(current,new,newconfirm):
    if sql_commands.checkpass(data[0],data[10],current):
        if new!=newconfirm:
            CTkMessagebox.messagebox(title='Error', text='Passwords do not match.', sound='on', button_text='OK')
        else:
            sql_commands.changepass(new,data[0])
            CTkMessagebox.messagebox(title='Successful', text='Password changed successfully', sound='on', button_text='OK')
    root1.destroy()

def changepassword():
    global root1
    root1=ctk.CTk()
    root1.title("Change Password")
    root1.geometry("1200x800")
    root1.state('zoomed')
    root1.grid_rowconfigure(0, weight=1)
    root1.grid_columnconfigure(0, weight=1)

    entry_current_password=ctk.CTkEntry(root1,placeholder_text="Enter Current Password",width=300)
    entry_current_password.pack(pady=20)
    entry_new_password=ctk.CTkEntry(root1,placeholder_text="Enter New Password",width=300)
    entry_new_password.pack(pady=20)
    confirm_new_password=ctk.CTkEntry(root1,placeholder_text="Confirm New Password",width=300)
    confirm_new_password.pack(pady=20)
    ctk.CTkButton(root1,text="Change Password",command=lambda:checkpassword(entry_current_password.get(),entry_new_password.get(),confirm_new_password.get())).pack(pady=20)
    root1.mainloop()

def change_details():
    def verify_password():
        current_password = entry_password.get()
        if current_password == data[1]:  # Check against stored password
            password_window.destroy()
            open_update_window()
            
        else:
            CTkMessagebox.messagebox(title='Error', text='Incorrect Password', sound='on', button_text='OK')
    
    def open_update_window():
        global root2
        root2 = ctk.CTk()
        root2.title("Change User Details")
        root2.geometry("600x600")
        root2.resizable(False, False)

        ctk.CTkLabel(root2, text="Change User Details", font=("Arial", 20, "bold")).pack(pady=20)

        # Existing user details
        existing_full_name = f"{data[2]} {data[3]}"  # Assuming index 2 is fname and index 3 is lname
        existing_dob = data[4]  # Date of Birth
        existing_gender = data[5]  # Gender
        existing_hostel = data[6]  # Hostel
        existing_room = data[7]  # Room No.
        existing_phone = data[8]  # Phone number
        existing_emergency_phone = data[9]  # Emergency Phone No.
        existing_email = data[10]  # Email ID

        entry_name = ctk.CTkEntry(root2, placeholder_text="Full Name", width=300)
        entry_name.insert(0, existing_full_name)
        entry_name.pack(pady=10)

        entry_dob = ctk.CTkEntry(root2, placeholder_text="Date of Birth (YYYY-MM-DD)", width=300)
        entry_dob.insert(0, existing_dob)
        entry_dob.pack(pady=10)

        entry_gender = ctk.CTkOptionMenu(root2, values=["Male", "Female"], command=None)
        entry_gender.set(existing_gender)
        entry_gender.pack(pady=10)

        entry_hostel = ctk.CTkEntry(root2, placeholder_text="Hostel", width=300)
        entry_hostel.insert(0, existing_hostel)
        entry_hostel.pack(pady=10)

        entry_room = ctk.CTkEntry(root2, placeholder_text="Room No.", width=300)
        entry_room.insert(0, existing_room)
        entry_room.pack(pady=10)

        entry_phone = ctk.CTkEntry(root2, placeholder_text="Phone No.", width=300)
        entry_phone.insert(0, existing_phone)
        entry_phone.pack(pady=10)

        entry_emergency_phone = ctk.CTkEntry(root2, placeholder_text="Emergency Phone No.", width=300)
        entry_emergency_phone.insert(0, existing_emergency_phone)
        entry_emergency_phone.pack(pady=10)

        entry_email = ctk.CTkEntry(root2, placeholder_text="Email ID", width=300)
        entry_email.insert(0, existing_email)
        entry_email.pack(pady=10)

        ctk.CTkButton(root2, text="Update Details", command=lambda: sql_commands.update_user_details(data[0], {
            'name': entry_name.get(),
            'dob': entry_dob.get(),
            'gender': entry_gender.get(),
            'hostel': entry_hostel.get(),
            'room': entry_room.get(),
            'phone': entry_phone.get(),
            'emergency_phone': entry_emergency_phone.get(),
            'email': entry_email.get()
        })).pack(pady=20)

        root2.mainloop()
    
    # Password prompt window
    password_window = ctk.CTk()
    password_window.title("Confirm Password")
    password_window.geometry("300x200")
    password_window.resizable(False, False)

    ctk.CTkLabel(password_window, text="Enter your password to continue:", font=("Arial", 14)).pack(pady=20)

    entry_password = ctk.CTkEntry(password_window, placeholder_text="Password", show='*', width=200)
    entry_password.pack(pady=10)

    ctk.CTkButton(password_window, text="Submit", command=verify_password).pack(pady=20)

    password_window.mainloop()


def userprofile(regno, email):
    global data
    data = sql_commands.getalldata(regno, email)
    root = ctk.CTk()
    root.title("User Profile")
    root.state('normal')
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(root,text="USER PROFILE",font=("ALGERIAN",30,"bold"),fg_color='transparent').pack(pady=20)

    text = ctk.CTkTextbox(root, width=100, height=100,font=("Comic Sans MS",19),state='disabled')
    text.pack(fill='both', expand=True)

    ctk.CTkButton(root,text="Change Password",command=changepassword).pack(pady=10)
    ctk.CTkButton(root,text="Change Details",command=change_details).pack(pady=10)
    ctk.CTkButton(root,text="Back",command=root.destroy).place(x=10,y=10)
    if data[5]=="M":
        x,y="Male","Men"
    else:
        x,y="Female","Women"
    data_a={"Registration No.":data[0],"Name":f"{data[2]} {data[3]}","Date of Birth":data[4],"Gender":x,f"{y}'s Hostel":data[6],"Room No.":data[7],"Phone No.":data[8],"Emergency Phone No.":data[9],"Email ID":data[10]}

    if data_a:
        text.configure(state='normal')
        for item in data_a:
            text.insert("end", str(item)+": "+str(data_a[item]) + "\n\n")
        text.configure(state='disabled')

    else:
        text.insert("end", "No data found or an error occurred.\n")
    
    root.mainloop()

userprofile('24BIA0019','ritesh.chaudhary@example.com')