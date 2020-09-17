import mysql
from mysql.connector import errorcode


class Database:

    conn = None
    instance = None

    @staticmethod
    def get_instance():
        if Database.instance is None:
            Database.instance = Database()
        return Database.instance

    def __init__(self, host='sh4ob67ph9l80v61.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='slfy8mk1fy7fhqb3', password='bb14oor3sjqs6ot1', db='wxjw05a7yqc6owjg'):

        try:
            conn = mysql.connector.connect(
                host=host, user=user, password=password, db=db)
            conn.autocommit = True
            self.conn = conn

        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(errorcode)
    """
    execute
    """

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor
