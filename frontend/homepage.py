import customtkinter as ctk
import time
import faq
import contact

def update_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    current_time_label.configure(text=current_time)
    root.after(1000, update_time)

def notice(notices, text_widget):
    text_widget.configure(state='normal')
    text_widget.delete('1.0', ctk.END)  # Clear previous notices
    for i, notice in enumerate(notices):
        text_widget.insert(ctk.END, f"{i + 1}) {notice}\n")
    text_widget.configure(state='disabled')

# Initialize the CustomTkinter main window
ctk.set_appearance_mode("System")  # Use "Dark" or "Light"
ctk.set_default_color_theme("blue")  # Set the color theme

root = ctk.CTk()  # Use CustomTkinter's CTk instead of Tk
root.title('Home Page')
root.geometry("1200x800")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

button_frame = ctk.CTkFrame(root, fg_color='lightgrey')
button_frame.pack(side=ctk.LEFT, fill=ctk.Y)

main_content = ctk.CTkFrame(root, fg_color='white')
main_content.pack(side=ctk.RIGHT, expand=True, fill=ctk.BOTH)

# VHub Label
main_label = ctk.CTkLabel(main_content, text="VHub", fg_color='white', text_color='black', width=10, height=2, font=('Helvetica', 40, 'bold'))
main_label.pack(pady=(20, 0))

slogan_label = ctk.CTkLabel(main_content, text="A Place to Connect", fg_color='white', text_color='black', width=10, height=2, font=('Helvetica', 30, 'bold'))
slogan_label.pack(pady=(20,0))
# Server Time
server_time_label = ctk.CTkLabel(button_frame, text="Server Time:", fg_color='lightgrey', text_color='black', font=('Arial', 16))
server_time_label.pack(pady=(15, 0))

current_time_label = ctk.CTkLabel(button_frame, fg_color='lightgrey', text_color='black', font=('Arial', 16))
current_time_label.pack(pady=(0, 15))

update_time()

# Buttons
academics_button = ctk.CTkButton(button_frame, text="Academics")
academics_button.pack(pady=10)

services_button = ctk.CTkButton(button_frame, text="Services")
services_button.pack(pady=10)

forums_button = ctk.CTkButton(button_frame, text="Forums")
forums_button.pack(pady=10)

faq_button = ctk.CTkButton(button_frame, text="FAQ",command=faq.faq)
faq_button.pack(pady=10)

contact_button = ctk.CTkButton(button_frame, text="Contact",command=contact.contact)
contact_button.pack(pady=10)

home_button = ctk.CTkButton(button_frame, text="Home Button")
home_button.pack(pady=10)

# Notice Board Section
board_label = ctk.CTkLabel(main_content, text="Notice Board", font=("Arial", 30, 'bold'), fg_color='white',text_color='black')
board_label.pack(pady=(20, 0))

# Create a frame for different sections
section_frame = ctk.CTkFrame(main_content, fg_color='white')
section_frame.pack(pady=(0, 20), fill=ctk.BOTH, expand=True)

# Academic Notices Section
academic_label = ctk.CTkLabel(section_frame, text="Academic Notices", font=("Arial", 20, 'bold'), fg_color='white', text_color='black')
academic_label.pack(pady=(10, 0))

academic_text = ctk.CTkTextbox(section_frame, height=5, width=80, font=("Arial", 16), state='disabled')
academic_text.pack(pady=(0, 10), fill=ctk.BOTH, expand=True)

academic_notices = ['Midterm Exams on March 1', 'Project submission deadline: April 15']
notice(academic_notices, academic_text)

# General Notices Section
general_label = ctk.CTkLabel(section_frame, text="General Notices", font=("Arial", 20, 'bold'), fg_color='white', text_color='black')
general_label.pack(pady=(10, 0))

general_text = ctk.CTkTextbox(section_frame, height=5, width=80, font=("Arial", 16), state='disabled')
general_text.pack(pady=(0, 10), fill=ctk.BOTH, expand=True)

general_notices = ['Welcome to the new semester!', 'Library hours updated: 9 AM - 9 PM']
notice(general_notices, general_text)

root.mainloop()
