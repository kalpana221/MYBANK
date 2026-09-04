from dbconnection import getconnection

def insertdata():
    print("enter customer data: ")
    cid = int(input("enter id: "))
    cname = input("enter name: ")
    caccno = int(input("enter AccNumber: "))
    cpassword = cname[:3]+"@123"
    cbalance = float(input("enter balance: "))

    conn = getconnection()
    cmd = conn.cursor()
    query = "insert into customers values(%s,%s,%s,%s,%s)"
    cmd.execute(query,(cid,cname,caccno,cpassword,cbalance))
    print("data inserted sucessfully!!!!!!!!")
    conn.commit()
    conn.close()
