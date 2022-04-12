from utility import clearscreen, findDatabase, findTables, getAllDatabases
from database import Database
from table import Table

def databaseController():
    
    db = None
    
    clearscreen()
    print("""
            Welcome to the Database Manager!
            
            What would you like to do today?
            
            (C)reate a new database
            (L)oad a pre-existing database
          """)
    dbChoice = input("Option: ").upper()
    
    clearscreen()
    
    if(dbChoice == "C"):
        dbName = input("What would you like to call your Database: ")
        db = Database(dbName)
    
    if(dbChoice == "L"):
        # Show Available Databases
        databases = getAllDatabases()
        print("Available Databases: ")
        for database in databases:
            print(database)
        
        dbName = input("\nWhat is the name of your database: ")
        if(findDatabase(dbName) == True):
            db = Database(dbName)
        else:
            print("Your Database does not exist!")
            create = input("Would you like to create a database with that name(Y/N): ").upper()
            if(create == "Y"):
                db = Database(dbName)
                
    return db