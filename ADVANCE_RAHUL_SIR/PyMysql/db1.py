import pymysql

try:
    con_obj=pymysql.connect(
    user="root",
    password="root",
    host="localhost"
    )
    print(con_obj)
    
except Exception as e:
    print(e)
