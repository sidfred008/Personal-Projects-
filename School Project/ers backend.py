def events():

    import mysql.connector as ms
    mydb  = ms.connect(username = 'root', host = 'localhost', password = 'HBFASV2022-23', database = 'registration')
    mycursor = mydb.cursor()
    c = "y"
    while c == "y":
        a = int(input("Enter the serial number: "))
        b = input("Enter the name of the event: ")
        c = input("Enter the date of the event scheduled: ")
        query = 'INSERT INTO events values(%s, %s, %s)'
        mycursor.execute(query, (a,b,c))
        mydb.commit()
        c = input("Do you still want to continue? (y/n): ")
    mydb.close()
events()

def participant():

    import mysql.connector as ms
    mydb = ms.connect(username = 'root', host = 'localhost', password = 'HBFASV2022-23', database = 'registration')
    mycursor = mydb.cursor()
    c = "y"
    while c == "y":
        b = input("Enter your Name: ")
        x = input("Enter whether you want to participate in the event as a participant or not in yes/no: ")
        z = input("Enter your mobile number: ")
        query = 'insert into participants values(%s, %s, %s)'
        mycursor.execute(query, (b,x,z))
        mydb.commit()
        c = input("Do you still want to continue? (y/n): ")
    mydb.close()
participant()

def attendees():
    import mysql.connector as ms
    mydb = ms.connect(username = "root", host = "localhost", password = "HBFASV2022-23", database = 'registration')
    mycursor = mydb.cursor()
    c = "y" 
    while c == "y":
        choice = input("Have you already registered before as a participant? (y/n): ")
        if choice == "y":
            print("Sorry , but you cannot register yourself twice as a participant and that too as an attendee: ")
            break
        else:
            Name = input("Enter your name: ")
            Mobile = input("Enter your mobile number: ")
            query = 'insert into attendees values (%s, %s,)'
            mycursor.execute(query, (Name, Mobile))
            mydb.commit()
            c = input("do you still want to register? (y/n): ")
    mydb.close()
attendees()



