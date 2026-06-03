# Creating a Table  Inside a database
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

    # create table sept3.std_info , It can directly create std_info table in the sept3 database
    cur_obj.execute("create table sept3.std_info(name varchar(20),usn varchar(20),age int(3),degree varchar(20),yop int(4),marks int(5),address varchar(20))")

    print("Table is Created")


    
except Exception as e:
    print(e)