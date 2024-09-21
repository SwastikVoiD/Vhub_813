import customtkinter as ctk
import sql_commands
def faq():
    root = ctk.CTk()  # Use CustomTkinter's CTk instead of Tk
    root.title("FAQ")
    root.geometry("1200x800")
    root.configure(fg_color='white')

    # Fetch FAQs from the database
    qa = sql_commands.faq_qa()

    main_label = ctk.CTkLabel(root, text="Frequent Questions and Answers", text_color='lightblue', font=("Algerian", 25, "bold"))
    main_label.pack(pady=25)

    for i, (question, answer) in enumerate(qa):
        question_label = ctk.CTkLabel(root, text=f"Question {i + 1}) {question}", font=("Comic Sans MS", 12, "bold"), text_color='black')
        question_label.pack(anchor="w", pady=(5, 0))

        answer_label = ctk.CTkLabel(root, text="Answer: " + answer, font=("Comic Sans MS", 12), text_color='black')
        answer_label.pack(anchor="w", pady=(0, 10))

    root.mainloop()
