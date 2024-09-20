import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Table Example")
root.geometry("600x400")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Question", "Answer"), show="headings")

# Define headings
tree.heading("Designation", text="Designation")
tree.heading("Name", text="Name")
tree.heading("Email ID",text="Email ID")
tree.heading("Phone No.",text="Phone No.")

# Define column widths
tree.column("Designation", width=300)
tree.column("Name", width=200)
tree.column("Email ID",width=200)
tree.column("Phone No.",width=100)

# Sample data
qa = [
    ("App not working", "Ok"),
    ("Hello", "Hi"),
    ("What is Python?", "A programming language"),
]

# Insert data into the table
for question, answer in qa:
    tree.insert("", tk.END, values=(question, answer))

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')

# Pack the treeview
tree.pack(expand=True, fill='both')

# Start the Tkinter event loop
root.mainloop()
