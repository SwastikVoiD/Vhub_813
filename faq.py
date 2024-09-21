import customtkinter as ctk
def faq():
    root = ctk.CTk()  # Use CustomTkinter's CTk instead of Tk
    root.title("FAQ")
    root.geometry("1200x800")

    root.configure(fg_color='white')
    qa = {
    "App not working": "Try restarting the app or checking your internet connection.",
    "Hello": "Hi there! How can we assist you today?"
    }
    main_label = ctk.CTkLabel(root, text="Frequent Questions and Answers", text_color='lightblue', font=("Algerian", 25, "bold"))
    main_label.pack(pady=25)

    for i, text in enumerate(qa):
        question_label = ctk.CTkLabel(root, text=f"Question {i + 1}) {text}", font=("Comic Sans MS", 12, "bold"), text_color='black')
        question_label.pack(anchor="w", pady=(5, 0))

        answer_label = ctk.CTkLabel(root, text="Answer: " + qa[text], font=("Comic Sans MS", 12), text_color='black')
        answer_label.pack(anchor="w", pady=(0, 10))

    root.mainloop()
