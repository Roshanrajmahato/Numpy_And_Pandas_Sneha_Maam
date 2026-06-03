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
    # Adding Multiple Value inside the table 

    # Now Reading a Data from Table 
    cur_obj.execute("select * from std_info")

    for data in cur_obj:
        print(data)
    
except Exception as e:
    print(e)