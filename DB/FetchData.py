# import pymysql

# def CreateConn():
#     return pymysql.connect(host="localhost",database="krishna",user="root",password="",port=3306)

# # def FetchAllData():
# #     conn=CreateConn()
# #     cursor=conn.cursor()
# #     query='''
# #     select * from stu
# #     '''
# #     cursor.execute(query)
# #     result=cursor.fetchall()
# #     for i in result:
# #         print(i)
    
# # FetchAllData()
# '''
# (1, 'Krishna', 'kana.sonkh@gmail.com', 'Sonkh Mathura')
# (2, 'kana', 'k@g.com', 'Mathura 281123')
# '''

# #fetch By Id


# # def FetchAllDataId(id):
# #     conn=CreateConn()
# #     cursor=conn.cursor()
# #     args=(id)
# #     query='''
# #     select * from stu where id=%s
# #     '''
# #     cursor.execute(query,args)
# #     result=cursor.fetchall()
# #     # print(result[0][1])
# #     for i in result:
# #         print("your Id is %d "%i[0])
# #         print("your Name is %s "%i[1])
# #         print("your Email is %s "%i[2])
# # id=int(input("enter id "))
# # FetchAllDataId(id)


# from pymysql import *

# def CreateConn():
#     return connect(host="localhost",database="krishna",user="root",password="",port=3306)
# def showAllData():
#     conn=CreateConn()
#     cursor=conn.cursor()
#     query="select * from stu"
#     cursor.execute(query)
#     result=cursor.fetchall()
#     print(result)
# showAllData()
