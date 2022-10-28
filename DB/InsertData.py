# import pymysql

# def CreateConnection():
#     return pymysql.connect(host="localhost",database="krishna",user="root",password="",port=3306)
# def InsertData(name,email,address):
#     conn=CreateConnection()
#     cursor=conn.cursor()
#     args=(name,email,address)
#     query='''
#     insert into stu(name,email,address) values(%s,%s,%s)
#     '''
#     cursor.execute(query,args)
#     conn.commit()
#     print("Data Inserted : ")
#     conn.close()
# name=input("Enter Name : ")
# email=input("Enter Email : ")
# ad=input("Enter Address : ")
# InsertData(name,email,ad)



# print("my name is %s",("krishna"))
# print("my age is %d",(18))
# print("my marks is %f",(18.6))

# def num(name,age,marks):
#     args=(name,age,marks)
#     print("my name is %s and my age is %d and my marks is %f"%args)

# name=input("enter Name ")
# age=int(input("enter age "))
# marks=float(input("enter float "))

# num(name,age,marks)
# name="krishna"
# print(f"{name}")
