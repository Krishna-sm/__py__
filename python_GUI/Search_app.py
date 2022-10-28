from tkinter import *
import pymysql
import tkinter.messagebox as msg
try:
    conn=pymysql.connect(host="localhost",database="tkinter",user="root",password="",port=3306)
except:
    if not conn:
        print("not connected")

r=Tk()

def click():
    cursor=conn.cursor()
    try:
        id=int(es.get())
        query='select * from contact where id=%s'
        args=(id)
        cursor.execute(query,args)
        result=cursor.fetchall()
        for i in result:
             ln=Label(r,text=i,font="50")
             ln.pack(padx=50,pady=90)
        conn.commit()
        conn.close()
    except:
            msg.showerror("no record","No record found")
    # name="Hello "+es.get()
    # ln=Label(r,text=name,font="50")
    # ln.pack(padx=50,pady=90)
r.geometry("500x200")
r.title("Search App ")
r.configure(bg="grey")

# Entry
es=Entry(r,width="40")
es.place(x=100,y=50)
bt1=Button(r,text="submit",padx="4",pady="2",command=click)
bt1.place(x=360,y=50)

mainloop()