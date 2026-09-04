from dbconnection import getconnection
from admindashboard import adminDashboard
def adminLogin():
    print("Welcome Admin\n--------------")
    checkuser = input("enter user name: ")
    checkpass = input("enter password: ")

    conn = getconnection()
    cmd = conn.cursor()
    cmd.execute("select * from admin where user=%s and password=%s",)
    res = cmd.fetchone()
    if res == None:
        print("Wrong credentional's!!!!")
        adminLogin()
    else:
        print("Login success")
        adminDashboard()