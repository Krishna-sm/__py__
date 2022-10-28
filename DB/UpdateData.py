import pymysql

def createConn():
    return pymysql.connect(host="localhost",database="krishna",user="root",password="",port=3306)

def ShowAllData():
    conn=createConn()
    cursor=conn.cursor()
    query="select * from stu"
    cursor.execute(query)
    res= cursor.fetchall()
    for i in res:
        print(i)

def UpdateData(name,email,address,id):
    conn=createConn()
    cursor=conn.cursor()
    query="update stu set name=%s,email=%s,address=%s where id=%s"
    args=(name,email,address,id)
    cursor.execute(query,args)
    print("Data Has Been Updated ")
    conn.commit()
    conn.close()

ShowAllData()
id=int(input("Enter student Id : "))
name=input("Enter student Name : ")
email=input("Enter student email : ")
address=input("Enter student address : ")
UpdateData(name,email,address,id)
ShowAllData()

