from asyncore import write
import csv
from document import Document

# This is our mock DB table that we will use for basic
# functionality such as CRUD.
class Table: 
    def __init__(self, name="users"):
        # Class variables.
        self.data = []
        self.size = 0
        self.name = name
    
    def getHeaders(self):
        print("\nHeaders for the table must be seperated by a comma.")
        print("Example: Email, First Name, Last Name, Phone Number, Message\n")
        headers= input("Enter Headers Here: ")
        self.headers = headers.split(',')

    
    # Function to query our table data. 
    def getDocument(self, keyToCheck="Email", query="*"):
        results = []
        
        # Get all Documents.
        if query == "*":
            for document in self.data:
                resultDocument = document.passData()
                results.append(resultDocument)
        
        else:
            # Go through documents stored in our table.
            for document in self.data:
                # Convert Document object to a dictionary so we can access and change it.
                resultDocument = document.passData()
                
                # Check if Document matches our query.
                if(resultDocument[keyToCheck] == query):
                    # Should only ever be 1 email so we should just return the document itself.
                    if(keyToCheck == "Email"):
                        return resultDocument
                    # Otherwise there could be many users sharing info such as multiple people with the first name John.
                    else:
                        results.append(resultDocument)
        
        # Return Results
        print("\nResults:\n")
        for document in results:
            for key in document:
                print("{} : {}".format(key, document[key]))
            print("\n")
            
    
    
    # Function to insert documents.
    def addDocument(self, data, hasEmail=False, emailKey = "Email"):
        if(hasEmail):
            # Email should be unique for each user so we
            # are going to check if email already exists.
            emailAlreadyExists = False
            
            # Iterate through Documents.
            for document in self.data:
                
                # Check if email exists
                document = document.passData()
                if document["Email"] == data["Email"]:
                    # If does set to true then break.
                    emailAlreadyExists = True
                    break
            
            # If our check came back true then we tell the user.        if emailAlreadyExists:
                print("\nEmail is already in use!!!\n")
        
        # Document does not have an email.
        else:
            # Add the document then update counter.    
            self.data.append(Document(data, self.headers))
            self.size += 1
            print("\n\n")
            self.printTable()
            
            # Return True so we can check in main if we
            # got an error.
            # True == Good       String == Bad
            return True
    
    # TODO: Possibly make functions for updating the email by itself and just making a Document function for that.
    # How we update Documents.
    #
    # updateKey: Key to check in the document. i.e. email, phone number
    # updateAt: The value we are checking for at updateKey, so if
    #           updateKey = "email" and updateAt = "dwalker9@my.brigevalley.edu"
    #           then update that document with the new data(newData).
    # newData: The data we are going to fill our document with.  
    def updateDocument(self, updateKey, updateAt, newData):
        for document in self.data:
            documentData = document.passData()
            if(documentData[updateKey] == updateAt):
                document.updateData(newData)
    
    # Function to print our table in a nicer format.
    def printTable(self):
        for document in self.data:
            # Have to use passData() since you can't print objects or iterate through them, but we can a dictionary.
            document = document.passData()
            for key in document:
                print(key, ":", document[key])
            print("\n")
                
    def createDocumentByInput(self):
        document = {}
        
        for key in self.headers:
        # Get data from user.
            document[key] = input("Enter {}: ".format(key))
            
        # Return Document.
        return document
    
    # Deletes a document based off it's email.
    def deleteDocument(self, data, keyToCheck="Email"):
        for i in range(len(self.data)):
            document = self.data[i].passData()
            if(document[keyToCheck] == data):
                self.data.pop(i)
        return True
    
    # Saves the current table to a csv.
    def saveTable(self, dbName):
        with open(dbName + "/" + self.name + ".csv", "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(self.data[0].passData().keys())
            for document in self.data:
                document = document.passData()
                writer.writerow(document.values())
