from tkinter import *

r=Tk()
r.title("Desgine")
r.geometry("500x500")
r.configure(bg="grey",border=10)

#========--------------> labels
fn=Label(r,text="First Name ").place(x=20,y=20)
ln=Label(r,text="Last Name ").place(x=20,y=60)
en=Label(r,text="EMail Address ").place(x=20,y=100)
cn=Label(r,text="Contact No ").place(x=20,y=140)


#========--------------> Entries
fne=Entry(r).place(x=120,y=20)
lne=Entry(r).place(x=120,y=60)
ene=Entry(r).place(x=120,y=100)
cne=Entry(r).place(x=120,y=140)

#========--------------> Buttons
b1=Button(r,text="Insert ",padx=20).place(x=20,y=180)
b2=Button(r,text="Update ",padx=20).place(x=120,y=180)
b3=Button(r,text="Select ",padx=20).place(x=220,y=180)
b4=Button(r,text="Delete ",padx=20).place(x=320,y=180)






mainloop()