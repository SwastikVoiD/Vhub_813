import tkinter as tk

root=tk.Tk()
root.title("FAQ")
root.config(bg='lightgrey')
root.geometry("1200x800")

qa={"App not working ":"ok ","hello":"hi"}
main_label=tk.Label(root,text="Frequent Questions and Answers",bg='lightgrey',font=("Algerian",25,"bold"))
main_label.pack(pady=25)
for i, text in enumerate(qa):
    label1=tk.Label(root,text=f"Question {i+1}) {text}",font=("Comic Sans MS",12,"bold"),bg='lightgrey')
    label1.pack(anchor="w",pady=5)
    label2 = tk.Label(root, text="Answer: "+qa[text],font=("Comic Sans MS",12),bg='lightgrey')
    label2.pack(anchor="w",pady=5)

root.mainloop()