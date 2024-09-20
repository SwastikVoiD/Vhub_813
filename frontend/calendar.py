import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar")
        self.selected_date = tk.StringVar()

        # Create Calendar
        self.calendar = Calendar(self.root, selectmode='day', year=2024, month=9, day=20)
        self.calendar.pack(pady=20)

        # Add Button to Get Selected Date
        self.show_date_button = ttk.Button(self.root, text="Show Selected Date", command=self.show_date)
        self.show_date_button.pack(pady=10)

        # Label to display selected date
        self.date_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.date_label.pack(pady=20)

        # Frame for adding events
        self.event_frame = ttk.Frame(self.root)
        self.event_frame.pack(pady=10)

        self.event_entry = tk.Entry(self.event_frame, width=30)
        self.event_entry.pack(side=tk.LEFT, padx=5)

        self.add_event_button = ttk.Button(self.event_frame, text="Add Event", command=self.add_event)
        self.add_event_button.pack(side=tk.LEFT)

        self.events_label = tk.Label(self.root, text="Events on this date:", font=("Helvetica", 14))
        self.events_label.pack(pady=10)

        self.events_display = tk.Text(self.root, height=10, width=50)
        self.events_display.pack(pady=10)

        self.events = {}

    def show_date(self):
        self.selected_date.set(self.calendar.get_date())
        self.date_label.config(text=f"Selected Date: {self.selected_date.get()}")

        # Show events for the selected date
        self.display_events()

    def add_event(self):
        date = self.calendar.get_date()
        event = self.event_entry.get()
        if event:
            if date not in self.events:
                self.events[date] = []
            self.events[date].append(event)
            self.event_entry.delete(0, tk.END)
            self.display_events()

    def display_events(self):
        date = self.calendar.get_date()
        self.events_display.delete(1.0, tk.END)
        if date in self.events:
            for event in self.events[date]:
                self.events_display.insert(tk.END, f"- {event}\n")
        else:
            self.events_display.insert(tk.END, "No events for this date.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
