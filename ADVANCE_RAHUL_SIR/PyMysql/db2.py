import pymysql

try:
    # con_obj :- To established the connection between the python and  with the help of connect()
    con_obj=pymysql.connect(
    user="root",
    password="12345",
    host="localhost"
    )
    
    # cur_obj :- For Move Inside a 
    cur_obj=con_obj.cursor()

    con_obj.execute("show databases")

    for db in con_obj:
        print(db)
    
except Exception as e:
    print(e)