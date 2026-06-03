# Creating a Table  Inside a database
# If we Perform CRUD Operation Then 
import pymysql

try:
    # con_obj :- To established the connection between the python and MySql Software with the help of connect()
    con_obj=pymysql.connect(
    user="root",
    password="root",
    host="localhost",
    database="sept3"
    )
    
    # cur_obj :- To established the connection between the MySql Databases With the help of cursor() method
    cur_obj=con_obj.cursor()

    # Creating a New Database In The MySql 
    # cur_obj.execute("create database sept3")

    # "std_info" Table is already created "std_info"
    # Adding User Input Multiple Value inside the table 

    name=input("Enter The Student Name")
    usn=input("Enter The usn Number ")
    age=input("Enter The age ")
    degree=input("Enter The degree ")
    yop=input("Enter The yop ")
    marks=input("Enter The marks")
    address=input("Enter The address")


    cur_obj.execute("insert into std_info(name,usn,age,degree,yop,marks,address) values(%s,%s,%s,%s,%s,%s,%s)",(name,usn,age,degree,yop,marks,address))

    con_obj.commit() # As we are performing CRUD Operation So we have to commit it with connection object
    
    print("User Input Multiple Data Is Added")


    
except Exception as e:
    print(e)