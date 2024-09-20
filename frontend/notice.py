import tkinter as tk
from tkinter import messagebox

def notice(x,y):
    y.config(state='normal')
    for i,x in enumerate(x):
        y.insert(tk.END,f"{i+1}) {x}\n")
    y.config(state='disabled')


root=tk.Tk()
root.title("Notice Board")
root.configure(bg='lightgrey')
root.geometry("1200x800")

board_label=tk.Label(root,text="Notice Board",font=("Arial",30,'bold'),bg='lightgrey')
board_label.pack(pady=20)

board_text=tk.Text(height=30,width=100,font=("Arial",15),state='disabled')
board_text.pack(pady=20)
l=['hello','bye','how are you']
notice(l,board_text)
root.mainloop()