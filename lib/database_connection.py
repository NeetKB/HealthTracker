import os, psycopg
from flask import g
from psycopg.rows import dict_row


# This class helps us interact with the database.
# It wraps the underlying psycopg library that we are using.


class DatabaseConnection:
    DEV_DATABASE_NAME = "health_tracker"
    TEST_DATABASE_NAME = "health_tracker_test"

    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    # This method connects to PostgreSQL using the psycopg library. We connect
    # to localhost and select the database name given in argument.
    def connect(self):
        try:
            db_name = self._database_name()
            print(f"Connecting to database: {db_name}")  # This will show which database is being connected to       
            self.connection = psycopg.connect(
                f"postgresql://amani:admin@localhost/{self._database_name()}",
                row_factory=dict_row)
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database {self._database_name()}! " \
                    f"Did you create it using `createdb {self._database_name()}`?")
        print(f"connected to db") 

    # This method seeds the database with the given SQL file.
    # We use it to set up our database ready for our tests or application.
    def seed(self, sql_filename):
        print(f"SQL Filename: {sql_filename}") 
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    

    # This method executes an SQL query on the database.
    def execute(self, query, params=[]):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = '' \
        'DatabaseConnection.exec_params: Cannot run a SQL query as ' \
        'the connection to the database was never opened. Did you ' \
        'make sure to call first the method DatabaseConnection.connect` ' \
        'in your app.py file (or in your tests)?'

    # This private method checks that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)

    # This private method returns the name of the database we should use.
    def _database_name(self):
        if self.test_mode:
            return self.TEST_DATABASE_NAME
        else:
            return self.DEV_DATABASE_NAME

# This function integrates with Flask to create one database connection that
# Flask request can use. 
def get_flask_database_connection(app):
    if not hasattr(g, 'flask_database_connection'):
        g.flask_database_connection = DatabaseConnection(
            test_mode=((os.getenv('APP_ENV') == 'test') or (app.config['TESTING'] == True))
        )
        g.flask_database_connection.connect()
    return g.flask_database_connection