import customtkinter as ctk
import travel
import vlx

def service():
    root = ctk.CTk()
    root.title("Service Menu")
    root.geometry("800x600")
    root.configure(fg_color='white')

    label = ctk.CTkLabel(root, text="Select a Service", text_color='black', font=('Comic Sans MS', 24))
    label.pack(pady=20)

    travelpool_button = ctk.CTkButton(root, text="Travel Pool", command=travel.travelpool)
    travelpool_button.pack(pady=10)

    vlx_button = ctk.CTkButton(root, text="VLX Service", command=vlx.vlx)
    vlx_button.pack(pady=10)

    root.mainloop()