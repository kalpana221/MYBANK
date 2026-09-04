import mysql.connector

def getconnection():
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "bank"
    );
    return con