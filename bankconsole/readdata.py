from dbconnection import getconnection

def readdata():

    conn = getconnection()
    cmd = conn.cursor()
    query = "select c_id,c_name,c_accno,c_balance from customers;"
    cmd.execute(query)
    result = cmd.fetchall()
    print("customers Data :\n")
    for row in result:
        print(row)
    conn.commit()
    conn.close()