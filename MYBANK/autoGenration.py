import random
from db import getConnection

def genrateAccNo():
     while True:
          
          accno = random.randint(1000000000,9999999999)

          conn = getConnection()
          cmd = conn.cursor(dictionary=True)
          cmd.execute("SELECT * FROM CUSTOMER WHERE accno=%s",(accno,))
          res = cmd.fetchone() #if accno not thier you will get None
          conn.close()
          if res == None:
               return accno
          
          
def genrateTransactionId():
     while True:
          
          tid = random.randint(50000,10000000000)

          conn = getConnection()
          cmd = conn.cursor()
          cmd.execute("SELECT * FROM TRANSACTIONS WHERE transactionID=%s",(tid,))
          res = cmd.fetchone() #if accno not thier you will get None
          conn.close()
          if res == None:
               return tid
     

          
          
          