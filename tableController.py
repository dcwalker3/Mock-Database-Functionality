from utility import clearscreen
from document import Document
from table import Table

def tableController(db, tableName):
    # Clear the screen.
    clearscreen()
    
    # Get the user input and figure out what they want to do.
    print("What Would you like to do?")
    print("""
            (C)reate User Document
            (R)etrieve User Document
            (U)pdate User Document
            (D)elete User Document
            
            (S)how All User Documents
            
            if you want to exit and save type (E)xit
            """)
    
    # We make this uppercase so we can use it in our switch.
    option = input("Enter Option: ").upper()
    
    # If the was C we allow them to create a user new document.
    if(option == "C"):
        clearscreen()
        
        # Create a new Document then add it to our users table.
        document = db.tables[tableName].createDocumentByInput()
        db.tables[tableName].addDocument(document)
        print("\n\n")
    
    # If they want to retrieve a document.
    elif(option == "R"):
        clearscreen()
        
        # Figure out what key we are looking for. i.e. email or first name
        print("What would you like to search for?")
        print("""
                (E)mail
                (F)irst Name
                (L)ast Name
                (P)hone Number
                (M)essage
                """)
        
        searchType = input("Enter Option: ").upper()
        
        # Let them input the term they are looking for.
        # So if they entered "E"
        # They could query test@mail.com
        if(searchType == "E"):
            clearscreen()
            email = input("Enter Email: ")
            results = db.tables[tableName].getDocument(keyToCheck="email",query=email)
        
        elif(searchType == "F"):
            clearscreen()
            firstName = input("Enter First Name: ")
            results = db.tables[tableName].getDocument(keyToCheck="firstName",query=firstName)
        
        elif(searchType == "L"):
            clearscreen()
            lastName = input("Enter Last Name: ")
            results = db.tables[tableName].getDocument(keyToCheck="lastName",query=lastName)
        
        elif(searchType == "P"):
            clearscreen()
            phoneNumber = input("Enter Phone Number: ")
            results = db.tables[tableName].getDocument(keyToCheck="phoneNumber",query=phoneNumber)
        
        elif(searchType == "M"):
            clearscreen()
            message = input("Enter Message: ")
            results = db.tables[tableName].getDocument(keyToCheck="message",query=message)
        
        else:
            clearscreen()
            print("Invalid Option!")
    
    # Update a user document.
    elif(option == "U"):
        clearscreen()
        
        # Do they want to update the whole document or just a field of it.
        print("Do you want to update (A)ll of the user document or just a (P)artial piece of it")
        updateOption = input("\nEnter Choice Here: ").upper()
        
        clearscreen()
        
        # Get the document they want to update based off email.
        userEmail = input("Please enter the users email here: ")
        
        # getDocument when passed (keyToCheck = "email") should return only 1 document.
        user = db.tables[tableName].getDocument(keyToCheck="email", query=userEmail)
        
        # Returns an empty array if no user was found.
        if(user == []):
            print("\n\nNO USERS EXIST WITH THIS EMAIL!!!")
            input()
            clearscreen()
        
        # User was found so now we update.
        else:
            # Just have them create a new document so we can just update our document with that.
            if(updateOption == "A"):
                clearscreen()
                document = db.tables[tableName].createDocumentByInput()
                user.updateData(document)
                
            # Else ask them what key to update and update that 1 key.
            elif(updateOption == "P"):
                print("Which field would you like to update: \n")
                print("(E)mail")
                print("(F)irst Name")
                print("(L)ast Name")
                print("(P)hone Number")
                print("(M)essage")
                
                updateAtKey = input("Enter Choice Here: ").upper()
                data = input("What would you like this field to contain: ")
                print("\n\n")
                
                if(updateAtKey == "E"):
                    user.updateKey("email", data)
                elif(updateAtKey == "F"):
                    user.updateKey("firstName", data)
                elif(updateAtKey == "L"):
                    user.updateKey("lastName", data)
                elif(updateAtKey == "P"):
                    user.updateKey("phoneNumber", data)
                elif(updateAtKey == "M"):
                    user.updateKey("message", data)
                else:
                    print("INVALID INPUT!!!")
                
                print("User {} was successfully updated".format(user.email))
    
    elif(option == "D"):
        clearscreen()
        
        # Get the document they want to update based off email.
        userEmail = input("Please enter the users email here that you wish to delete: ")
        
        # getDocument when passed (keyToCheck = "email") should return only 1 document.
        user = db.tables[tableName].getDocument(keyToCheck="email", query=userEmail)
        
        # Returns an empty array if no user was found.
        if(user == []):
            print("\n\nNO USERS EXIST WITH THIS EMAIL!!!")
            input()
            clearscreen()
        
        # User was found so now we delete.
        else:
            db.tables[tableName].deleteDocument(user["email"])
            
    elif (option == "S"):
        clearscreen()
        db.tables[tableName].printTable()
        input()
    
    elif(option == "E"):
        clearscreen()
        return False
    
    return True