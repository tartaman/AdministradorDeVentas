import mysql.connector
class Conector:
    def __init__(self):
        self.conection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="opticavictor", port="3306")
        self.cursor = self.conection.cursor()
