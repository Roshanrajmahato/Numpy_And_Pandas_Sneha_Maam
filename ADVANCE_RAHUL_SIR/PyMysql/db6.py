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

    qry="insert into std_info(name,usn,age,degree,yop,marks,address) values(%s,%s,%s,%s,%s,%s,%s)"

    values=[
        ('harshith','JSS234',16,'Btech',2025,70,'Bangalore'),
        ('raj','RJS234',18,'Bsc',2035,89,'Bankog'),
        ('Vivek','JYU234',19,'Bcom',2021,27,'Dhanbad'),
        ('harshith','JSS234',21,'Mtech',2020,23,'Chennai'),
        ('rahul','GHE234',17,'Masters',2022,65,'Mumbai')
        
        ]
    
    cur_obj.executemany(qry,values)
    con_obj.commit() # As we are performing CRUD Operation So we have to commit it with connection object
    print(cur_obj.rowcount,"rows are added")
    print("Multiple Data Is Added")


    
except Exception as e:
    print(e)