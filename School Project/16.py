import mysql.connector as ms

mydb = ms.connect(username = 'root' , password = 'HBFASV2022-23', host = 'localhost', database = 'registration')
mycursor = mydb.cursor()

def create_events():
    n = int(input("Enter how many records you want to enter inside the table as the host of the event: "))
    for i in range(n):
        Sno = int(input("Enter the serial number of the event: "))
        Event = input("Enter the name of the event: ") 
        scheduled_date = input("Enter the scheduled date: ") 
        tickets = input("Enter the total number of tickets available: ")
        query = 'INSERT INTO events values(%s, %s, %s, %s)'
        mycursor.execute(query, (Sno,Event,scheduled_date,tickets))
        mydb.commit()

def create_participants():
    n = int(input("Enter the number of participants' record you want to enter inside the database: "))
    for i in range(n):
        Sno = int(input("Enter the serial number of the participant: "))
        Name = input("Enter the name of the participant: ")
        mobile = input("Enter the mobile number of the partcipant: ")
        query = 'INSERT INTO participants values(%s, %s, %s)'
        mycursor.execute(query, (Sno, Name, mobile))
        mydb.commit()

def create_attendees():
    n = int(input("Enter the number of attendees' records you want to enter inside the database: "))
    for i in range(n):
        Sno = int(input("Enter the serial number of the attendees: "))
        Name = input("Enter the name of the attendees: ")
        mobile = input("Enter the mobile number of the attendee: ")
        anyone_else = int(input("Enter the number of member(s) with the attendee if any:  "))
        query = 'INSERT INTO attendees values (%s, %s, %s, %s)'
        mycursor.execute(query, (Sno, Name, mobile, anyone_else))
        mydb.commit()

def update_ticket_availability():
    Event = input("Enter the name of the event: ")
    tickets = int(input("Enter the new number of available tickets: "))

    query = 'UPDATE events SET tickets = %s WHERE Event = %s'
    mycursor.execute(query, (tickets, Event))
    mydb.commit()
    print("Available tickets updated successfully!")

def show_events():
    mycursor.execute("SELECT*from events; ")
    events = mycursor.fetchall()
    for event in events:
        print(event)

def show_participants():
    mycursor.execute("SELECT*from participants; ")
    participants = mycursor.fetchall()
    for participant in participants:
        print(participant)

def show_attendees():
    mobile = input("Enter mobile number to check user details: ")
    mycursor.execute("SELECT * FROM participants WHERE mobile = %s", (mobile,))
    user_details = mycursor.fetchall()

    if user_details:
        print("User details found:")
        for user in user_details:
            print(user)

    else:
        print("User not found. Please register first.")

while True:
    print("\n\t-----------|EVENT REGISTRATION AND MANAGEMENT SYSTEM|-----------\t")
    print("1.) Events/hosts")
    print("2.) Participants")
    print("3.) Attendees")
    print("4.) Tickets for the event")
    print("5.) Show Events")
    print("6.) Show Participants")
    print("7.) Show Attendees")
    ch = int(input("Enter out of the following options given to you who are you and according to that fill in the following fields: "))

    if ch == 1:
        create_events()
    elif ch == 2:
        create_participants()
    elif ch == 3:
        create_attendees()
    elif ch == 4:
        update_ticket_availability()
    elif ch == 5:
        show_events()
    elif ch == 6:
        show_participants()
    elif ch == 7:
        show_attendees()
    elif ch == 8:
        break
    else:
        print("invalid option")



