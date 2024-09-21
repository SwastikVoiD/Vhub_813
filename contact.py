import customtkinter as ctk

def contact():
    # Initialize the main window
    root = ctk.CTk()  
    root.title("Hostel Contacts")
    root.geometry("800x600")

    # Create a main frame for the scrollable content
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill='both', expand=True)

    # Create a canvas for scrolling
    canvas = ctk.CTkCanvas(main_frame)
    scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
    scrollable_frame = ctk.CTkFrame(canvas)

    # Configure the scrollable frame
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Men's Hostel Title
    men_label = ctk.CTkLabel(scrollable_frame, text="MEN'S HOSTEL", font=("Comic Sans MS", 18, "bold"))
    men_label.grid(row=0, column=0, columnspan=4, pady=10)

    # Men's Hostel Staff Data
    men_data = [
        ("Director, Men's Hostel", "Dr. M. Shiva Shankar", "director.mh@vit.ac.in", "0416 - 220 2520"),
        ("Chief Warden, Men's Hostel", "Dr. R. Mohanasundaram", "cw.mh@vit.ac.in", "0416 – 220 2521"),
        ("Associate Chief Warden, Men's Hostel", "Dr. S. Sivakumar", "acw.mh@vit.ac.in", "0416 – 220 2522"),
        ("Associate Chief Warden, Men's Hostel", "Dr. A. Sathiavelu", "acw1.mh@vit.ac.in", "0416 – 220 2522"),
        ("Warden (Discipline)", "Dr. S. Dinesh Kumar", "warden.discipline@vit.ac.in", "0416 - 220 2528"),
        ("Warden (Attendance)", "Dr. Senthilnathan P", "warden.attendance@vit.ac.in", "0416 - 220 2528"),
        ("Warden (Food)", "Dr. Hemadri Reddy Reganti", "warden.food@vit.ac.in", "0416 - 220 2528"),
        ("Warden (Events)", "Dr. Karthikeyan J", "warden.events@vit.ac.in", "0416 - 220 2528"),
        ("Administrative Officer - Men's Hostel", "Mr. Kumaravel P", "ao.mh@vit.ac.in", "0416 - 220 2523"),
        ("Manager, Men's Hostel", "Mr. K. Ravichandran", "manager.mh@vit.ac.in", "0416 - 220 2523"),
        ("Assistant Manager - Food Men's Hostel", "Mr. D. Varadharajan", "asstmanager.food@vit.ac.in", "0416 - 220 2528"),
        ("Assistant Manager -1 Men's Hostel", "Mr. Bhoobalan K", "asstmanager1.mh@vit.ac.in", "0416 - 220 2526"),
        ("Assistant Manager - 2 Men's Hostel", "Mr. Chidambaram N", "asstmanager2.mh@vit.ac.in", "0416 - 220 2525"),
        ("Men's Hostel Office Staff", "Mr. R. Senthil Kumar\nMr. S. Ramalingam\nMr. Venkatesan S\nMr. K.R. Shankar Ganesh\nMr. Samuvel A", "N/A", "0416 - 220 2525 / 2526"),
        ("Men's Hostel Office Senior Supervisor", "(24 hours X 7 days)", "N/A", "0416 - 220 2524"),
        ("Men's Hostel Office - Security Guard", "(24 hours X 7 days)", "N/A", "0416 - 220 2527"),
    ]

    # Populate Men's Hostel Data
    for idx, (title, name, email, phone) in enumerate(men_data):
        ctk.CTkLabel(scrollable_frame, text=title, font=("Comic Sans MS", 12, "bold")).grid(row=idx + 1, column=0, padx=5, pady=2, sticky='w')
        ctk.CTkLabel(scrollable_frame, text=name).grid(row=idx + 1, column=1, padx=5, pady=2, sticky='w')
        ctk.CTkLabel(scrollable_frame, text=email).grid(row=idx + 1, column=2, padx=5, pady=2, sticky='w')
        ctk.CTkLabel(scrollable_frame, text=phone).grid(row=idx + 1, column=3, padx=5, pady=2, sticky='w')

    # Ladies' Hostel Title
    ladies_label = ctk.CTkLabel(scrollable_frame, text="LADIES' HOSTEL", font=("Comic Sans MS", 18, "bold"))
    ladies_label.grid(row=len(men_data) + 1, column=0, columnspan=4, pady=10)

    # Ladies' Hostel Staff Data
    ladies_data = [
        ("Director, Ladies Hostels", "Dr. P. Deepa Sankar", "director.lh@vit.ac.in", "0416 – 220 2712"),
        ("Chief Warden, Ladies Hostels", "Dr. G. S. Nirmala", "cw.lh@vit.ac.in", "0416 - 220 2713"),
        ("Associate Chief Warden", "Dr. S. Mythili", "acw.lh@vit.ac.in", "0416 - 220 2895"),
        ("Hostel Manager", "Ms. R. Reshma", "manager.lh@vit.ac.in", "0416 - 220 2893"),
        ("Assistant Manager", "Dr. K. Saranya", "lh.am@vit.ac.in", "0416 - 220 2706"),
        ("Assistant Manager", "Ms. S. Dhanam", "lh.am1@vit.ac.in", "0416 - 220 2710"),
        ("Section Supervisor", "Ms. G. Subbulakshmi", "lh@vit.ac.in", "0416 - 220 2710 / 2711"),
        ("Transport", "Ms. R. Padma", "padma.r@vit.ac.in", "9488839864"),
    ]

    # Populate Ladies' Hostel Data
    for idx, (title, name, email, phone) in enumerate(ladies_data):
        ctk.CTkLabel(scrollable_frame, text=title, font=("Comic Sans MS", 12, "bold")).grid(row=len(men_data) + idx + 2, column=0, padx=5, pady=2, sticky='w')
        ctk.CTkLabel(scrollable_frame, text=name).grid(row=len(men_data) + idx + 2, column=1, padx=5, pady=2, sticky='w')
        ctk.CTkLabel(scrollable_frame, text=email).grid(row=len(men_data) + idx + 2, column=2, padx=5, pady=2, sticky='w')
        ctk.CTkLabel(scrollable_frame, text=phone).grid(row=len(men_data) + idx + 2, column=3, padx=5, pady=2, sticky='w')

    # Start the main loop
    root.mainloop()

