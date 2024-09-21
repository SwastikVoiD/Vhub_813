import customtkinter as ctk

# Initialize the CustomTkinter application
root = ctk.CTk()

# Set the title of the window
root.title("Maximized Window Example")

# Maximize the window
root.state('normal')  # Set to normal first
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # Set to full screen dimensions

# Add some widgets (for demonstration)
label = ctk.CTkLabel(root, text="This window is maximized.", font=("Arial", 20))
label.pack(pady=20)

# Start the main loop
root.mainloop()
