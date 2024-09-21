import customtkinter as ctk
import time
import faq
import contact
import services
import forum
import userprofile

def update_time(current_time_label):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    current_time_label.configure(text=current_time)
    current_time_label.after(1000, update_time, current_time_label)

def notice(notices, text_widget):
    text_widget.configure(state='normal')
    text_widget.delete('1.0', ctk.END)  # Clear previous notices
    for i, notice in enumerate(notices):
        text_widget.insert(ctk.END, f"{i + 1}) {notice}\n")
    text_widget.configure(state='disabled')

def homepage(a,b):
    global regno,email
    regno,email=a,b
    root = ctk.CTk()
    root.title('Home Page')
    root.geometry("1200x800")
    root.attributes('-fullscreen',True)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    

    button_frame = ctk.CTkFrame(root, fg_color='lightgrey')
    button_frame.pack(side=ctk.LEFT, fill=ctk.Y)

    main_content = ctk.CTkFrame(root, fg_color='white')
    main_content.pack(side=ctk.RIGHT, expand=True, fill=ctk.BOTH)

    ctk.CTkLabel(main_content, text="VHub", fg_color='white', text_color='black', width=10, height=2, font=('Helvetica', 40, 'bold')).pack(pady=(20, 0))

    ctk.CTkLabel(main_content, text="A Place to Connect", fg_color='white', text_color='black', width=10, height=2, font=('Helvetica', 30, 'bold')).pack(pady=(20, 0))

    # Server Time
    server_time_label = ctk.CTkLabel(button_frame, text="Server Time:", fg_color='lightgrey', text_color='black', font=('Arial', 16))
    server_time_label.pack(pady=(15, 0))

    current_time_label = ctk.CTkLabel(button_frame, fg_color='lightgrey', text_color='black', font=('Arial', 16))
    current_time_label.pack(pady=(0, 15))

    update_time(current_time_label)

    ctk.CTkButton(button_frame, text="Scheduling").pack(pady=10)
    ctk.CTkButton(button_frame, text="Services",command=services.service).pack(pady=10)
    ctk.CTkButton(button_frame, text="Forums",command=lambda:forum.forum(regno)).pack(pady=10)
    ctk.CTkButton(button_frame, text="FAQ", command=faq.faq).pack(pady=10)
    ctk.CTkButton(button_frame, text="Contact", command=contact.contact).pack(pady=10)
    ctk.CTkButton(button_frame, text="User Profile",command=lambda:userprofile.userprofile(regno,email)).pack(pady=10)
    ctk.CTkLabel(main_content, text="Notice Board", font=("Arial", 30, 'bold'), fg_color='white', text_color='black').pack(pady=(20, 0))

    section_frame = ctk.CTkFrame(main_content, fg_color='white')
    section_frame.pack(pady=(0, 20), fill=ctk.BOTH, expand=True)

    ctk.CTkLabel(section_frame, text="Academic Notices", font=("Arial", 20, 'bold'), fg_color='white', text_color='black').pack(pady=(10, 0))

    academic_text = ctk.CTkTextbox(section_frame, height=5, width=80, font=("Arial", 16), state='disabled')
    academic_text.pack(pady=(0, 10), fill=ctk.BOTH, expand=True)

    academic_notices = ['Midterm Exams on March 1', 'Project submission deadline: April 15']
    notice(academic_notices, academic_text)

    ctk.CTkLabel(section_frame, text="General Notices", font=("Arial", 20, 'bold'), fg_color='white', text_color='black').pack(pady=(10, 0))

    general_text = ctk.CTkTextbox(section_frame, height=5, width=80, font=("Arial", 16), state='disabled')
    general_text.pack(pady=(0, 10), fill=ctk.BOTH, expand=True)

    general_notices = ['Welcome to the new semester!', 'Library hours updated: 9 AM - 9 PM']
    notice(general_notices, general_text)

    root.mainloop()

