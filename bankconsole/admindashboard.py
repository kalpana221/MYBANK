from dbconnection import getconnection

def createcustomer():
    print("please enter customer details: ")
    cid = int(input("enter customer id: "))
    cname = input("enter customer name: ")
    cmobile = int(input("enter mobile no: "))
    caccno = int(input("enter accno: "))
    #cpass = cname[:3] + str(cmobile)[:3]
    cpass = "test@123"
    cbalance = float(input("enter balance: "))

    conn = getconnection
    cmd = conn.cursor()
    cmd.execute("insert customer values(%s,%s,%s,%s,%s,%s)",(cid,cname,cmobile,caccno,cpass,cbalance))
    print("data is inserted!!!!")
    conn.commit()
    conn.close()

def deletecustomer():
    print("please enter customer details: ")
    cid = int(input("enter customer id: "))

    conn = getconnection
    cmd = conn.cursor()
    cmd.execute("delete from customers where c_id=%s",(cid,))
    print("customer is deleted!!!!")
    conn.commit()
    conn.close()



def updatecustomer():
    pass
def adminDashboard():
    pass
def viewcustomer():
    print("view customer details: ")
    conn = getconnection
    cmd = conn.cursor()
    cmd.execute("select * from customers;")
    result = cmd.fetchall()
    for row in result:
        print(row)
    conn.commit()
    conn.close()
def changepassword():
    pass



    print("Welcome admin\n------------")
    print("1.create customer")
    print("2.delete customer")
    print("3.update customer")
    print("4.view customers")
    print("5.change your password")
    print("6.Exit")

    option = int(input("enter your option: "))
    while True:
        if option == 1:
            createcustomer()
        elif option == 2:
            deletecustomer()
        elif option == 3:
            updatecustomer()
        elif option == 4:
            viewcustomer()
        elif option == 5:
            changepassword()
        elif option == 6:
            print("byee admin!!!!!1")
            break
        else:
            print("please enter valid option try again")