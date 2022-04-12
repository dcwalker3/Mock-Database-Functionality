from operator import indexOf
from os import mkdir
from table import Table
from utility import *

class Database:
    # Initialize our database.
    def __init__(self, name=""):
        self.tables = {}
        self.name = name
        self.numberOfTables = 0
        self.numberOfDocuments = 0
    
    
    # Function to create a table.
    def createTable(self, name, data=[]):
        self.tables[name] = Table()
        self.tables[name].name = name
        self.tables[name].data = data
        self.tables[name].size = len(data)
        self.tables[name].getHeaders()
        self.numberOfTables += 1
        self.numberOfDocuments += len(data)
    
    # Function that asks user to create a table.
    # Created this function in case I ever have a need to
    # create multiple tables at once I will call createTable(), but
    # if a user only needs 1 I call this function instead.
    def createTablePrompt(self):
        tableName = input("What would you like to name the table: ")
        self.createTable(tableName)
    
    # Function to delete a table from a database.
    def deleteTable(self, name):
        del self.tables[name]
        self.numberOfTables -= 1
        self.numberOfDocuments -= len(self.tables[name].data)
    
    # Get table by name.
    def getTable(self, name):
        return self.tables[name]
    
    # How we load a premade table.
    def loadTable(self, tableName):
        # Create Table object.
        self.tables[tableName] = Table()
        self.tables[tableName].name = tableName
        self.tables[tableName].data = []
        self.tables[tableName].size = 0
        self.numberOfTables += 1
        
        # Created a empty array so we could save the data but not the headers.
        csvData = []
        # Read data from our CSV file (Table).
        with open("{}.csv".format(tableName), "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                csvData.append(line)
                self.tables[tableName].size += 1
        
        self.tables[tableName].headers = csvData[0]
        
        # Write all data to the table except the headers.
        for i  in range(1, len(csvData)):
            self.tables[tableName].data.append(csvData[i])
        
        def loadTables(self):
            tables = []
            dbTables = listdir(getcwd + "/" + self.name)
            for table in dbTables:
                self.tables[table[(indexOf('.')):]] = Table()
            for table in self.tables:
                self.loadTable(table)        
                    
    def selectTable(self):
        print("Please Select the table you want to use from the options listed below.")
        for table in self.tables:
            print(table.name)
    
    def saveDatabase(self):
        try:
            mkdir(self.name)
        except FileExistsError:
            pass
        
        print(self.tables)
        for table in self.tables:
            self.tables[table].saveTable(self.name)