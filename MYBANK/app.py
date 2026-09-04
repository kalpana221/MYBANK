from flask import Flask,request,jsonify,render_template,redirect
from db import getConnection
from autoGenration import genrateTransactionId,genrateAccNo

app = Flask("__name__")

# api for checking connection
@app.route("/")
def home():
     return render_template("index.html")

#creating customer url for createcustomer
@app.route("/createCustomer")
def createCustomerFun():
     return render_template("createCustomer.html")

#creating editCustomer
@app.route("/editCustomer/<caccno>",methods=["POST","GET"])
def editCustomer(caccno):
     
     conn = getConnection()
     cmd= conn.cursor(dictionary=True)
     cmd.execute('''
                 SELECT cname,cmobile,cemail,accno,password
                 FROM customer
                 WHERE accno=%s''',
                 (caccno,))
     data = cmd.fetchone()
     conn.close()
     print(data)
     return render_template("editCustomer.html",customer=data)


@app.route("/makeTransaction")
def makeTransaction():
     return render_template("transaction.html")


# api to insert customer data (working)
@app.route("/insertData",methods=["POST"])
def insertData():

     data = request.form
     
     cname = data["name"]
     cmobile = data["mobile"]
     cemail = data["email"]
     caccno = genrateAccNo()
     cbalance = data["balance"]
     password = "Test@123"
     
     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute('''
                 INSERT INTO CUSTOMER
                 (cname,cmobile,cemail,accno,balance,password) 
                 values 
                 (%s,%s,%s,%s,%s,%s);'''
                 ,(cname,int(cmobile),cemail,caccno,cbalance,password))
     conn.commit()
     conn.close()
     return redirect("/adminDashboard")

# api to delete customer data
@app.route("/deleteCustomer/<caccno>",methods=["GET","POST"])
def deleteCustomer(caccno):

     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute("DELETE FROM customer WHERE accno=%s",(caccno,))
     conn.commit()
     conn.close()
     return redirect("/adminDashboard")


# api to update the customer details
@app.route("/updateCustomer",methods=["POST"])
def updatecustomer():
     
     data = request.form
     caccno = data["caccno"]
     uname = data["uname"]
     umobile = data["umobile"]
     uemail = data["uemail"]
     upassword = data["upassword"]
     

     conn = getConnection()
     cmd = conn.cursor(dictionary=True)
     cmd.execute("SELECT cname,cmobile,cemail,password FROM customer")
     d = cmd.fetchone()
     conn.close()
     
     cname = d["cname"]
     cmobile = int(d["cmobile"])
     cemail  = d["cemail"]
     cpassword = d["password"]
     
     if uname == "":
          uname = cname
          
     if umobile == "":
          umobile = cmobile
          
     if uemail == "":
          uemail = cemail
          
     if upassword == "":
          upassword = cpassword
     
     

     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute('''
                 UPDATE CUSTOMER
                 SET
                 cname=%s,
                 cmobile=%s,
                 cemail=%s,
                 password=%s
                 where accno=%s''',
                 (uname,umobile,uemail,upassword,caccno))
     conn.commit()
     conn.close()
     
     return redirect("/adminDashboard")

# api to update the customer details
@app.route("/updateCustomer",methods=["POST"])
def updateCustomer():
     
     data = request.form
     caccno = data["caccno"]
     uname = data["uname"]
     umobile = data["umobile"]
     uemail = data["uemail"]
     upassword = data["upassword"]
     

     conn = getConnection()
     cmd = conn.cursor(dictionary=True)
     cmd.execute("SELECT cname,cmobile,cemail,password FROM customer")
     d = cmd.fetchone()
     conn.close()
     
     cname = d["cname"]
     cmobile = int(d["cmobile"])
     cemail  = d["cemail"]
     cpassword = d["password"]
     
     if uname == "":
          uname = cname
          
     if umobile == "":
          umobile = cmobile
          
     if uemail == "":
          uemail = cemail
          
     if upassword == "":
          upassword = cpassword
     
     

     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute('''
                 UPDATE CUSTOMER
                 SET
                 cname=%s,
                 cmobile=%s,
                 cemail=%s,
                 password=%s
                 where accno=%s''',
                 (uname,umobile,uemail,upassword,caccno))
     conn.commit()
     conn.close()
     
     return redirect("/adminDashboard")



# api for fetching all records from db
@app.route("/adminDashboard",methods=["GET"])
def viewAllCustomers():

     conn = getConnection()
     cmd = conn.cursor(dictionary=True)
     cmd.execute("SELECT sno,cname,cmobile,cemail,accno,balance FROM CUSTOMER")
     result = cmd.fetchall()
     conn.close()
     return render_template("adminDashboard.html",data=result)
     
# api for athentication of admin
@app.route("/adminLogin",methods=["POST"])
def adminLogin():
     
     data = request.form
     
     checkUser = data["username"]
     checkPassword = data["password"]
     
     conn = getConnection()
     cmd = conn.cursor()
     cmd.execute("SELECT * FROM ADMIN where username=%s and password=%s",(checkUser,checkPassword))
     result = cmd.fetchone()
     conn.close()
     
     if result == None:
          return render_template("index.html",message="Login Failed")
     else:
          return redirect("/adminDashboard")
     
     # 



# api for deposite to cutomer acc
@app.route("/transaction",methods=["POST"])
def deposite():
     data = request.form
     tranType = data["t_type"]
     caccno = data["caccno"]
     amt = float(data["amount"])
     tid = genrateTransactionId()
     
     conn = getConnection()
     cmd = conn.cursor(dictionary=True)
     cmd.execute("SELECT balance FROM CUSTOMER WHERE accno=%s;",(caccno,))
     data = cmd.fetchone()
     if data == None:
          return f"error : Accno not found! please check and try again!!!"
     
     if tranType=="deposite":
          # deposite means adding amt to existing balance
          cBalance = float(data["balance"])
          updatedB = cBalance + amt
     else:
          # withdraw means adding amt to existing balance
          cBalance = float(data["balance"])
          updatedB = cBalance - amt
           
          
     cmd.execute("UPDATE CUSTOMER SET balance=%s WHERE accno=%s;",(updatedB,caccno))
     conn.commit()
     
     cmd.execute('''
               INSERT INTO TRANSACTIONS
               (transactionID,transactionType,accno,balanceBeforeT,balanceAfterT)
               VALUES
               (%s,%s,%s,%s,%s);''',
               (tid,tranType,caccno,cBalance,updatedB))
     conn.commit()
     conn.close()
     
     return redirect("/adminDashboard")

if __name__ == "__main__":
     app.run(debug=True)
     