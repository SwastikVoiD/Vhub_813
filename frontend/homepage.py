import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    current_time_label.config(text=current_time)
    root.after(1000, update_time)

def notice(notices, text_widget):
    text_widget.config(state='normal')
    for i, notice in enumerate(notices):
        text_widget.insert(tk.END, f"{i + 1}) {notice}\n")
    text_widget.config(state='disabled')

root = tk.Tk()
root.title('Home Page')
root.geometry("1200x800")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.configure(bg='lightgrey')

button_frame = tk.Frame(root, bg='lightgrey', padx=10, pady=10)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

main_content = tk.Frame(root, bg='white')
main_content.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# VHub Label
main_label = tk.Label(main_content, text="VHub", bg='white', fg='black', width=10, height=2, font=('Helvetica', 40, 'bold'))
main_label.pack(pady=(20, 0))

# Server Time
server_time_label = tk.Label(button_frame, text="Server Time:", bg='lightgrey', fg='black', font=('Arial', 16))
server_time_label.pack(pady=(15, 0))

current_time_label = tk.Label(button_frame, bg='lightgrey', fg='black', font=('Arial', 16))
current_time_label.pack(pady=(0, 15))

update_time()

# Buttons
academics_button = tk.Button(button_frame, text="Academics")
academics_button.pack(pady=15)

services_button = tk.Button(button_frame, text="Services")
services_button.pack(pady=15)

forum_button = tk.Button(button_frame, text="Forums")
forum_button.pack(pady=15)

faq_button = tk.Button(button_frame, text="FAQ")
faq_button.pack(pady=15)

contact_button = tk.Button(button_frame, text="Contact")
contact_button.pack(pady=15)

home_button=tk.Button(button_frame,text="Home Button")
home_button.pack(pady=15)

# Notice Board Section
board_label = tk.Label(main_content, text="Notice Board", font=("Arial", 30, 'bold'), bg='white')
board_label.pack(pady=(20, 0))

# Create a frame for different sections
section_frame = tk.Frame(main_content, bg='white')
section_frame.pack(pady=(0, 20))

# Academic Notices Section
academic_label = tk.Label(section_frame, text="Academic Notices", font=("Arial", 20, 'bold'), bg='white')
academic_label.pack(pady=(10, 0))

academic_text = tk.Text(section_frame, height=5, width=80, font=("Arial", 12), state='disabled')
academic_text.pack(pady=(0, 10))

academic_notices = ['Midterm Exams on March 1', 'Project submission deadline: April 15']
notice(academic_notices, academic_text)

# General Notices Section
general_label = tk.Label(section_frame, text="General Notices", font=("Arial", 20, 'bold'), bg='white')
general_label.pack(pady=(10, 0))

general_text = tk.Text(section_frame, height=5, width=80, font=("Arial", 12), state='disabled')
general_text.pack(pady=(0, 10))

general_notices = ['Welcome to the new semester!', 'Library hours updated: 9 AM - 9 PM']
notice(general_notices, general_text)

root.mainloop()
