# import Database Api 
import pymysql

# create connection 
def CreateConnection():
    return pymysql.Connect(host="localhost",database="krishna",user="root",password="",port=3306)
     
# create table using python
def CreateTable():
    conn=CreateConnection() # stablish the conn
    cursor=conn.cursor() # create a curusor
    query='''
        create table stu(id int primary key auto_increment,name varchar(50),email varchar(50),address varchar(50))
    '''# query to be excuted
    cursor.execute(query) #excute the query
    conn.commit() # save the query in dbms
    print("Table is created ")
    conn.close()

#calling a function 
CreateTable()
