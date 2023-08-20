from pymongo import MongoClient
from bson.objectid import ObjectId

# Class definition, accessing & connecting to mongo database for a web based app.
class AACDatabaseLayer(object) :
    
    # Create Constructor
    def __init__(self, HOST, PORT, username, password) :
        self.host = HOST
        self.port = PORT 
        self.username = username
        self.password = password
        # Store all credentials in a single URI
        self.uri = 'mongodb://' + username + ':' + password + '@' + HOST + ':' + PORT
        print('uri: ' + self.uri)
        
    # Connect to DB
    def connect(self, logging=False) :
        self.connection = MongoClient(self.uri)
        if logging:
            #show the db
            print(self.connection.list_database_names())
            
    # Need to set current MONGO DB for query options (mongodb use command)
    # Parameters specifiy the db to use as a string:
    def setDatabase(self, database) :
        self.db = self.connection[database]
        
    # Complete Create method to implement the C in CRUD
    def create(self, collection, data) :
        if data is not None:
            # Data should be in dictionary
            insert_dictionary = self.db[collection].insert_one(data)
            if insert_dictionary != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty.")
            
    # Implement the read capability method to implement the R in CRUD
    # Like mongodb find/findOne() 
    # Specify collection as a string and specify the filter as a .py dictionary
    def read(self, collection, filter) :
        #Get collection
        c = self.db[collection]
        #find function
        return c.find()

