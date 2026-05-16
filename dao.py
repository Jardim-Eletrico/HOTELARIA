import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                database = "hotelaria",
                user = "root",
                password = ""
            )

            return self.connection
        except Error as e:
            print(f"Erro: {e}")
            return None
        
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=None): #INSERT, UDPATE E DELETE
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor
        except Error as e:
            if self.connection:
                self.connection.rollback()
            print(f"Erro ao executar query: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()

    def fetch_all(self, query, params=None): #BUSCAR VÁRIOS REGISTROS
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True) #DEFINE COMO DICIONÁRIO, FACILITA NAS BUSCAS
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Erro ao executar SELECT: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()

    def fetch_one(self, query, params=None): #BUSCAR APENAS UM REGISTRO
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True) #DEFINE COMO DICIONÁRIO, FACILITA NAS BUSCAS
            cursor.execute(query, params or ())
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Erro ao executar SELECT: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()