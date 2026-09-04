import mysql.connector

def getConnection():
     con = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database = "ourbank"
     )
     
     return con

def creatAdminTable():
     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute('''
                    create table IF NOT EXISTS admin(
                    sno int AUTO_INCREMENT PRIMARY KEY,
                    username varchar(20) NOT NULL,
                    password varchar(20) NOT NULL);
                 
                 ''')
     conn.commit()
     conn.close()
     
def createCustomerTable():
     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute('''
                    create table IF NOT EXISTS customer(
                    sno int AUTO_INCREMENT PRIMARY KEY,
                    cname varchar(20) NOT NULL,
                    cmobile NUMERIC(10) UNIQUE,
                    cemail varchar(30) UNIQUE,
                    accno NUMERIC(15) UNIQUE,
                    balance DECIMAL(10,2) DEFAULT 0,
                    password VARCHAR(20) NOT NULL);
                 
                 ''')
     conn.commit()
     conn.close()
     
def createTransactionTable():
     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute('''
                    CREATE TABLE IF NOT EXISTS TRANSACTIONS(
                    sno int AUTO_INCREMENT PRIMARY KEY,
                    transactionID NUMERIC(10) UNIQUE NOT NULL,
                    transactionType ENUM("deposite","withdraw") NOT NULL,
                    accno numeric(15) Not Null,
                    balanceBeforeT decimal(10,2) NOT NULL,
                    balanceAfterT decimal(10,2) NOT NULL,
                    transactionData date default (CURRENT_DATE),
                    trancsationTime time default (CURRENT_TIME),
                    FOREIGN KEY (accno)
                    REFERENCES CUSTOMER(accno)
                    ON DELETE CASCADE);
               
               ''')
     conn.commit()
     conn.close()
     
     
creatAdminTable()
createCustomerTable()
createTransactionTable()
print("Tables created go check")