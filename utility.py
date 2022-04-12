from os import system, listdir, path, getcwd


def clearscreen():
    if (system.__name__=="nt"):
        system("cls")
    else:
        system("clear")

def findDatabase(name):
    dirContents = listdir(getcwd())
    for file in dirContents:
        if file == name:
            return True
    return False

def findTables(dbName):
    Tables = []
    dbContents = listdir(getcwd() + "/" + dbName)
    for file in dbContents:
        if file.endswith(".csv"):
            Tables.append(file)
    return Tables    
    
def getAllDatabases():
    databases = []
    dirContents = listdir(getcwd())
    for file in dirContents:
        if(path.isdir(file) and file != "__pycache__"):
            databases.append(file)
    return databases

def getAllTables(dbName):
    tables = []
    dirContents = listdir(getcwd() + "/" + dbName)
    for file in dirContents:
        if(file.endswith('.csv') and file != "__pycache__"):
            tables.append(file)

def tableExists(db, tableName):
    for table in db.tables:
        if table.name == tableName:
            return True
    return False
