"""  Program to all the operation of python database connection in same program 
 Output:~
 Database Created
 Table is Created 
 User Input 
 ....
 ....

 ....

 Data is Added




"""

import pymysql

try:

    # For Connecting
    con_obj = pymysql.connect(
        user="root",
        password="root",
        host="localhost",
    )

    cur_obj = con_obj.cursor()

    # To Create a New DataBase
    cur_obj.execute('create database userdata')

    print("New Database Is Created")

    try:
        # Adding a Table in the Database
        cur_obj.execute(
            "create table userdata.user_info("
            "name varchar(20),"
            "age int(5),"
            "phone int(10),"
            "address varchar(20))"
        )

        print("table is created")

        NAME = input("Enter the name : ")
        AGE = int(input("Enter the age : "))
        PHONE = int(input("Enter the phone : "))
        ADDRESS = input("Enter the address : ")

        cur_obj.execute(
            "insert into userdata.user_info(name, age, phone, address) "
            "values (%s, %s, %s, %s)",
            (NAME, AGE, PHONE, ADDRESS)
        )

        con_obj.commit()

        print("Data is added")
    
    except Exception as e:
        print(e)


except Exception as e:
    print(e)
