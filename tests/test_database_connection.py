

"""
When I seed the database I get some records back 
"""

def test_database_connection(db_connection):

    db_connection.seed("seeds/database_connection_test.sql")
    
    db_connection.execute("INSERT INTO test_table (name) VALUES (%s)", ["second_record"])
    
    res = db_connection.execute("SELECT * FROM test_table")

    assert res == [{"id": 1, "name" : "first_record"}, {"id": 2, "name" : "second_record"}]


def test_real_database_connection(db_connection):

    db_connection.seed("seeds/database_connection.sql")
    
    db_connection.execute("INSERT INTO users (fullname, email, password) VALUES (%s, %s, %s)", ["Avnita", "av@example.com", "Pass123!"])
    
    res = db_connection.execute("SELECT * FROM users")

    assert res == [
        {"id": 1, "fullname" : "Sam", "email": "sam@example.com", "password" : "password123!"},
        {"id": 2, "fullname" : "Avnita", "email": "av@example.com", "password" : "Pass123!"}]
