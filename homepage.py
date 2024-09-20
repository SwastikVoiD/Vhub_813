import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    current_time_label.config(text=current_time)
    root.after(1000, update_time)

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
main_label = tk.Label(root, text="VHub",bg='white',fg='black', width=10, height=2,
                       font=('Helvetica', 40,'bold'))
main_label.place(x=450, y=0)

server_time_label = tk.Label(button_frame, text="Server Time:", bg='lightgrey', fg='black', font=('Arial', 16))
server_time_label.pack(pady=(15, 0))

current_time_label = tk.Label(button_frame, bg='lightgrey', fg='black', font=('Arial', 16))
current_time_label.pack(pady=(0, 15))

update_time()

academics_button = tk.Button(button_frame, text="Academics")
academics_button.pack(pady=15)

utilities_button=tk.Button(button_frame,text="Utilities")
utilities_button.pack(pady=15)

roomcheck_button=tk.Button(button_frame,text="Room Check")
roomcheck_button.pack(pady=15)

services_button=tk.Button(button_frame,text="Services")
services_button.pack(pady=15)

forum_button=tk.Button(button_frame,text="Forums")
forum_button.pack(pady=15)

faq_button=tk.Button(button_frame,text="FAQ")
faq_button.pack(pady=15)

contact_button=tk.Button(button_frame,text="Contact")
contact_button.pack(pady=15)

noticeboard_button=tk.Button(button_frame,text="Notice Board")
noticeboard_button.pack(pady=15)

halloffame_button=tk.Button(button_frame,text="Hall of Fame")
halloffame_button.pack(pady=15)

root.mainloop()