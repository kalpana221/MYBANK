from dbconnection import getconnection

def deletedata():
    print("enter customer data: ")
    cid = int(input("enter id: "))

    conn = getconnection()
    cmd = conn.cursor()
    query = "delete from customers where c_id = %s"
    cmd.execute(query,(cid))
    print("data deleted sucessfully!!!!!!!!")
    conn.commit()
    conn.close()