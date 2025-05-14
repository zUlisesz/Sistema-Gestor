import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host = 'myhost',
        user = 'username',
        password = 'password',
        database = 'namedb'
    )
    
#gotta set the correct values tu the entries of the function