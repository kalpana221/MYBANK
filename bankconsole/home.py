from dbconnection import getconnection
from adminlogin import adminLogin
from customerlogin import customerLogin
def home():
    print("Welcome To my Banck")
    print("choose one option:")
    print("1.Admin Login")
    print("2.customer Login")
    print(3.Exit)

    option = int(input("enter your option: "))
    if option == 1:
        adminLogin()
    elif option == 2:
        customerLogin()
    elif option == 3:
        print("Thank you visit again!!!")
    else:
        print("Please try again giving correct options")

home()