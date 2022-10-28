from tkinter import *
import tkinter.messagebox as msgBox
import pymysql

try:
    conn=pymysql.connect(host="localhost",database="tkinter",user="root",password="",port=3306)
except:
    print("not connected to the dataBase")



def InsertData():
    name=en.get()
    email=ee.get()
    mobile=em.get()
    if name=='' or email==''or mobile=='':
        msgBox.showerror("save","All feild Are Complusary")
    else:
        try:
            
            cursor=conn.cursor()
            query='insert into contact(name,email,mobile) values(%s,%s,%s)'
            args=(name,email,mobile)
            cursor.execute(query,args)
            msgBox.showinfo("Saved","Data Has Been Recorded ")
            conn.commit()
            conn.close()
        except:
            print("Not inserted an err")
        



r=Tk()
r.configure(bg="grey")
r.geometry("500x400")
r.title(" Contact Form ")
#----------> Label
# add label
n=Label(r,text="Name ",padx="20")
n.place(x=20,y=20)
e=Label(r,text="Email",padx="20")
e.place(x=20,y=60)
m=Label(r,text="Mobile ",padx="20")
m.place(x=20,y=100)
#----------> Entry Input Boxes
# add Inputs and entry

en=Entry(r)
en.place(x=200,y=20)
ee=Entry(r)
ee.place(x=200,y=60)
em=Entry(r)
em.place(x=200,y=100)

#add Button
bt1=Button(r,text="Save Data",padx="60",pady="5",font="sans-serif",command=InsertData)
bt1.place(x=100,y=150)

cursor2=conn.cursor()
query1='''
select * from contact
'''
cursor2.execute(query1)
results=cursor2.fetchall()
n=0
for i in results:
    dataLabel=Label(r,text=i,bg="white")
    n+=1
    dataLabel.pack(padx=150,pady=10*(n))



# print record in the database

mainloop()