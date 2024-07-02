import mysql.connector
class Conector:
    def __init__(self):
        self.conection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="")
        self.cursor = self.conection.cursor()
