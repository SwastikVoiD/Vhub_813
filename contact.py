import sql_commands
import customtkinter as ctk

def contact():
    root = ctk.CTk()
    root.title("Hostel Contacts")
    root.state('normal')
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.configure(fg_color='black')

    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill='both', expand=True)

    canvas = ctk.CTkCanvas(main_frame)
    scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
    scrollable_frame = ctk.CTkFrame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    try:
        contacts = sql_commands.contact_sql()
        for idx, (hostel_type, title, name, email, phone) in enumerate(contacts):
            ctk.CTkLabel(scrollable_frame, text=f"{hostel_type} - {title}", font=("Comic Sans MS", 12, "bold")).grid(row=idx, column=0, padx=5, pady=2, sticky='w')
            ctk.CTkLabel(scrollable_frame, text=name).grid(row=idx, column=1, padx=5, pady=2, sticky='w')
            ctk.CTkLabel(scrollable_frame, text=email).grid(row=idx, column=2, padx=5, pady=2, sticky='w')
            ctk.CTkLabel(scrollable_frame, text=phone).grid(row=idx, column=3, padx=5, pady=2, sticky='w')
    except Exception as err:
        print(f"Error: {err}")
    back_button=ctk.CTkButton(root,text="Back",command=root.destroy)
    back_button.pack(pady=5)
    root.mainloop()
