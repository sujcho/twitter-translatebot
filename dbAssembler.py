import sqlite3

class Assembler(object):
    def __init__(self, DB_model):
        self._DB_model = DB_model;

    def get_cfg_fromDB(self):
        """Return user list and cfgs"""

    def add_handle(self):
        """Add user handle """

    def get_userlist_fromDB(self):
        """get user """

class SQLAssembler(Assembler):
    def __init__(self, DB_model, database):
        #define a path to DB.
        #for SQL later,
        #self.database = database;
        super(SQLAssembler, self).__init__(DB_model)
        conn = sqlite3.connect(database)

    def add_handle(self):
        """Add user handle """

    #implment method
    def get_cfg_fromDB(self):
        #add implementation for SQL (ex. (select token)query,)
        cfg = {};
        return cfg;

#this supposed to read from DB
    def get_userlist_fromDB(self):
        #add implementation for SQL (ex. (select userlist)query,)
        user_list = ['25073877','838107760721985536']
        return user_list;
