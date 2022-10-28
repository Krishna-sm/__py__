
import pymysql



try:
    conn=pymysql.connect(host="localhost",database="krishna",user="root",password="")
    if conn:
        print("connection success")
except:
    print("Error not connected")

def CreateTable():
    cursor=conn.cursor()
    query='''
    create table emp(id int primary key auto_increment,name varchar(50),email varchar(50),address varchar(50))
    '''
    cursor.execute(query)
    print("table created ")
    conn.commit()
    conn.close()

def InsertData(name,email,address):
    cursor=conn.cursor()
    query=f'''
    insert into emp(name,email,address) values('{name}','{email}','{address}')
    '''
    cursor.execute(query)
    print("Data Is Inserted ")
    conn.commit()
    conn.close()

def FetchAllData():
    cursor=conn.cursor()
    query='select * from emp'
    cursor.execute(query)
    res=cursor.fetchall()
    for i in res:
        print(f"Name : {i[0]}")
        print(f"Email : {i[1]}")
        print(f"Address : {i[2]}")
    conn.commit()
    conn.close()
# CreateTable()

# name=input("Enter Name : ")
# email=input("Enter Email : ")
# address=input("Enter Address : ")

# InsertData(name,email,address)

FetchAllData()



