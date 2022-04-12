from turtle import clear
from databaseController import databaseController
from document import Document
from table import Table
from database import Database
from utility import clearscreen, findDatabase, findTables, tableExists
from tableController import tableController

def main():
    # Returns Database Object
    # Database Object has a name, a list of tables,
    # a number of tables, and a number of documents.
    db = databaseController()
    
    running = True
    tableName = None
    
    while(running):
        while(tableName == None):
            clearscreen()
            if len(db.tables) == 0:
                print("This Database has no tables!\n Please create a table below!\n")
                tableName = input(" What would you like to name your table: ")
            
            else:
                tables = findTables(db.name)
                print("Available Tables:\n")
                for table in tables:
                    print(table)
                
                tableName = input("\nWhat is the name of the table you wish to use: ")
                
                if(tableExists(db.name, tableName)):
                    print("\n\nUsing table {}!".format(tableName))
                    input()
                
                else:
                    print("\n\nThat table does not exist!\n\n")
                    input()
                    tableName = None
        
        db.createTable(tableName)        
            
            
        running = tableController(db, tableName)
        
    
    db.saveDatabase()

            
            
if __name__ == "__main__":
    main()