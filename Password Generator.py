import random #to import the random module for randomly generating characters from the list of characters

class passwordgenerator(): #defining the class passwordgenerator

    def __init__(self, passwords, characters, listOfCharacters ): #defining the constructor and data members for the class

        self.passwords = passwords
        self.characters = characters
        self.listOfCharacters = listOfCharacters

    def create_password(self): #defining the method for generating password
        
        
        for i in self.characters: #defining a loop to go inside the characters so that the loop variable is then appended inside the list

            self.listOfCharacters.append(i) 
        
        print(self.listOfCharacters)
        
        number = int(input("Enter how many characters you want inside your password:" ))

        for i in range(number):

            self.passwords = self.passwords + random.choice(self.listOfCharacters)

        print("Your random generated password is: " , self.passwords)

password_object = passwordgenerator("", "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_-+=|\'[]{}:;'""<>.,/?~`", [])
password_object.create_password()

