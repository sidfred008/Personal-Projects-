import mysql.connector as ms

mydb = ms.connect(username = 'root' , password = 'HBFASV2022-23', host = 'localhost', database = 'registration')
mycursor = mydb.cursor()

def create_events():

    n = int(input("Enter how many records you want to enter inside the table as the host of the event: "))
    for i in range(n):
        Event_id = int(input("Enter the event_id of the event: "))
        Event = input("Enter the name of the event: ") 
        scheduled_date = input("Enter the scheduled date: ") 
        tickets = input("Enter the total number of tickets available: ")
        query = 'INSERT INTO events values(%s, %s, %s, %s)'
        mycursor.execute(query, (Event_id,Event,scheduled_date,tickets))
        mydb.commit()

def create_participants():

    n = int(input("Enter the number of participants' record you want to enter inside the database: "))
    for i in range(n):
        Sno= int(input("Enter the serial number of the participant: "))
        Name = input("Enter the name of the participant: ")
        mobile = input("Enter the mobile number of the partcipant: ")
        event = input("Enter the event in which you'd like to take part in out of the following events available: ")
        query = 'INSERT INTO participants values(%s, %s, %s, %s)'
        mycursor.execute(query, (Sno, Name, mobile, event))
        mydb.commit()

def create_attendees():

    try:

        n = int(input("Enter the number of attendees' records you want to enter inside the database: "))
        for i in range(n):
            Sno = int(input("Enter the serial number of the attendee: "))
            Name = input("Enter the name of the attendees: ")
            mobile = input("Enter the mobile number of the attendee: ")
            anyone_else =  int(input("Enter the number of attendees whether someone is there with you or not: "))
            Event_choice = input("Enter the name of the event you'd like to attend: ")
            mycursor.execute("SELECT tickets FROM events WHERE Event = %s", (Event_choice,))
            event_info = mycursor.fetchone()

            if event_info and int(event_info[0]) > 0:
                query = 'INSERT INTO attendees VALUES (%s, %s, %s, %s, %s)'
                values = (Sno, Name, mobile, anyone_else, Event_choice)  
                mycursor.execute(query, values)
                mydb.commit()
                print("Registration successful for {}. Enjoy the event!".format(Name))
                mycursor.execute("UPDATE events SET tickets = tickets - 1 WHERE Event = %s", (Event_choice,))
                mydb.commit()

            else:
                print("Sorry, either the event '{}' does not exist or tickets are not available. Registration unsuccessful.".format(Event_choice))

    except Exception as e:
        print("Error: ", e)


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

    try:

        name = input("Enter mobile number to check the participants' details:  ").strip()[:20]
        mycursor.execute("SELECT*FROM participants where mobile like %s", (name, ))
        participants_details= mycursor.fetchall()
        print("EXECUTING QUERY: ","SELECT*FROM participants where mobile like %s", (name, ))

        if  participants_details:
            print("participant details found: ")
            for user in participants_details:
                print(user)
        
        else:
            print("Participant not found. Please register yourself first for the event to take part in it ")
    
    except Exception as e:
        print("Error: ", e)

def show_attendees():

    try:

        name = input("Enter mobile number to check the attendees' details: ").strip()[:20]
        mycursor.execute("SELECT*from attendees where mobile like %s", (name, ))
        user_details = mycursor.fetchall()
        print("EXECUTING QUERY: ", "SELECT*FROM attendees where mobile like %s", (name, ))

        if user_details:
            print("user details found: ")
            for user in user_details:
                print(user)
        
        else: 
            print("Attendee not found. Please register first")

    except Exception as e:
        print("Error: ", e)

while True:

    print("\n\t-----------| EVENT REGISTRATION AND MANAGEMENT SYSTEM |-----------\t")
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



