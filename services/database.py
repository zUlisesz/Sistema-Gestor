import mysql.connector

def connect_db():
    try: 
        conn = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'Interesting.Eminem',
            database = 'gestor',
            port = '3306'
        ) 
    except mysql.connector.Error as e:
        print(f'{e}')
        
    return conn

connect_db()