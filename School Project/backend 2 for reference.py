import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as ms

def connect_to_database():
    return ms.connect(user='root', host='localhost', password='HBFASV2022-23', database='registration')

def create_events_table():
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS events (serial_number INT, event_name VARCHAR(255), event_date VARCHAR(20))")

def create_participants_table():
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS participants (name VARCHAR(255), participate VARCHAR(5), mobile VARCHAR(10), event_name VARCHAR(255))")

def create_attendees_table():
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS attendees (name VARCHAR(255), mobile VARCHAR(10), event_name VARCHAR(255))")

def insert_event(serial_number, event_name, event_date):
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        query = 'INSERT INTO events VALUES (%s, %s, %s)'
        mycursor.execute(query, (serial_number, event_name, event_date))
        mydb.commit()

def insert_participant(name, participate, mobile, event_name):
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        query = 'INSERT INTO participants VALUES (%s, %s, %s, %s)'
        mycursor.execute(query, (name, participate, mobile, event_name))
        mydb.commit()

def insert_attendee(name, mobile, event_name):
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        query = 'INSERT INTO attendees VALUES (%s, %s, %s)'
        mycursor.execute(query, (name, mobile, event_name))
        mydb.commit()


def get_events():
    with connect_to_database() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM events")        
        return mycursor.fetchall()

class HostGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Host Registration")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label_serial_number = tk.Label(self.frame, text="Serial Number:")
        self.label_serial_number.grid(row=0, column=0, padx=5, pady=5)
        self.entry_serial_number = tk.Entry(self.frame)
        self.entry_serial_number.grid(row=0, column=1, padx=5, pady=5)

        self.label_event_name = tk.Label(self.frame, text="Event Name:")
        self.label_event_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_event_name = tk.Entry(self.frame)
        self.entry_event_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_event_date = tk.Label(self.frame, text="Event Date:")
        self.label_event_date.grid(row=2, column=0, padx=5, pady=5)
        self.entry_event_date = tk.Entry(self.frame)
        self.entry_event_date.grid(row=2, column=1, padx=5, pady=5)

        self.button_register_event = tk.Button(self.frame, text="Register Event", command=self.handle_event_registration)
        self.button_register_event.grid(row=3, column=0, columnspan=2, pady=10)

    def handle_event_registration(self):
        serial_number = int(self.entry_serial_number.get())
        event_name = self.entry_event_name.get()
        event_date = self.entry_event_date.get()
        insert_event(serial_number, event_name, event_date)
        messagebox.showinfo("Success", "Event registration successful!")

class ParticipantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Participant Registration")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label_name = tk.Label(self.frame, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_participate = tk.Label(self.frame, text="Participate (yes/no):")
        self.label_participate.grid(row=1, column=0, padx=5, pady=5)
        self.entry_participate = tk.Entry(self.frame)
        self.entry_participate.grid(row=1, column=1, padx=5, pady=5)

        self.label_mobile = tk.Label(self.frame, text="Mobile Number:")
        self.label_mobile.grid(row=2, column=0, padx=5, pady=5)
        self.entry_mobile = tk.Entry(self.frame)
        self.entry_mobile.grid(row=2, column=1, padx=5, pady=5)

        self.label_events = tk.Label(self.frame, text="Select Events:")
        self.label_events.grid(row=3, column=0, padx=5, pady=5)
        events = get_events()
        self.event_choices = [event[1] for event in events]
        self.selected_events = []
        self.checkbox_vars = [tk.IntVar() for _ in range(len(self.event_choices))]
        for i, event_name in enumerate(self.event_choices):
            checkbox = tk.Checkbutton(self.frame, text=event_name, variable=self.checkbox_vars[i])
            checkbox.grid(row=i + 3, column=1, padx=5, pady=5, sticky="w")
        self.button_register_participant = tk.Button(self.frame, text="Register Participant", command=self.handle_participant_registration)
        self.button_register_participant.grid(row=len(self.event_choices) + 3, column=0, columnspan=2, pady=10)

    def handle_participant_registration(self):
        name = self.entry_name.get()
        participate = self.entry_participate.get()
        mobile = self.entry_mobile.get()

        if validate_mobile(mobile):
            for i, event_name in enumerate(self.event_choices):
                if self.checkbox_vars[i].get():
                    insert_participant(name, participate, mobile, event_name)
            messagebox.showinfo("Success", "Participant registration successful!")
        else:
            messagebox.showerror("Error", "Invalid mobile number. Please enter a 10-digit numeric value.")

class AttendeeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendee Registration")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label_name = tk.Label(self.frame, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_mobile = tk.Label(self.frame, text="Mobile Number:")
        self.label_mobile.grid(row=1, column=0, padx=5, pady=5)
        self.entry_mobile = tk.Entry(self.frame)
        self.entry_mobile.grid(row=1, column=1, padx=5, pady=5)

        self.label_events = tk.Label(self.frame, text="Select Events:")
        self.label_events.grid(row=2, column=0, padx=5, pady=5)
        events = get_events()
        self.event_choices = [event[1] for event in events]
        self.selected_events = []
        self.checkbox_vars = [tk.IntVar() for _ in range(len(self.event_choices))]
        for i, event_name in enumerate(self.event_choices):
            checkbox = tk.Checkbutton(self.frame, text=event_name, variable=self.checkbox_vars[i])
            checkbox.grid(row=i + 2, column=1, padx=5, pady=5, sticky="w")
        self.button_register_attendee = tk.Button(self.frame, text="Register Attendee", command=self.handle_attendee_registration)
        self.button_register_attendee.grid(row=len(self.event_choices) + 2, column=0, columnspan=2, pady=10)

    def handle_attendee_registration(self):
        name = self.entry_name.get()
        mobile = self.entry_mobile.get()

        if validate_mobile(mobile):
            for i, event_name in enumerate(self.event_choices):
                if self.checkbox_vars[i].get():
                    insert_attendee(name, mobile, event_name)
            messagebox.showinfo("Success", "Attendee registration successful!")
        else:
            messagebox.showerror("Error", "Invalid mobile number. Please enter a 10-digit numeric value.")

def validate_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def main():
    create_events_table()
    create_participants_table()
    create_attendees_table()

    root = tk.Tk()
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10)

    label = tk.Label(main_frame, text="Choose Registration Type:")
    label.pack(pady=10)

    host_button = tk.Button(main_frame, text="Host", command=lambda: HostGUI(tk.Toplevel(root)))
    host_button.pack(pady=10)

    participant_button = tk.Button(main_frame, text="Participant", command=lambda: ParticipantGUI(tk.Toplevel(root)))
    participant_button.pack(pady=10)

    attendee_button = tk.Button(main_frame, text="Attendee", command=lambda: AttendeeGUI(tk.Toplevel(root)))
    attendee_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
