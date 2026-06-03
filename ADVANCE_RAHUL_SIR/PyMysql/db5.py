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

    # "std_info" Table is already created 
    # So Now we are Inserting the Value Inside The Table "std_info"
    cur_obj.execute("insert into setp.info(name,usn,age,degree,yop,marks,address) values('roshan','REC','-75','B.Tech',2000,95,'durga')")

    con_obj.commit() # As we are performing CRUD Operation So we have to commit it with connection object
    print("Data Is Added")


    
except Exception as e:
    print(e)