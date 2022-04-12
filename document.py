class Document:
    # Gets a Dictionary passed to it for data.
    def __init__(self, data, headers):
        self.data = {}
        self.headers = headers
        
        # Data we store in our Class.
        for key in self.headers:
            self.data[key] = data[key]
            
    # Update the data we have with new data.
    def updateData(self, data):
        self.data = data
    
    # Allows us to update only 1 field of the document instead of all of it.
    def updateKey(self, key, newData):
        for fieldKey in self.headers:
            if(fieldKey == key):
                self.data[key] = newData
        else:
            print("This key you attempted to enter is not available!")
        
     
    # Function that returns the documents data.
    # We use this as if we didn't and tried to return
    # print a document we would just get the standard
    # < Object Type at Memory Address > instead of data.  
    def passData(self):       
        # Return Document.
        return self.data
    
    