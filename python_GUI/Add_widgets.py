from tkinter import *

# create a main window
r=Tk()

#change nav title of main window
r.title("Krishna 😁")
#change the Geomatrial size
r.geometry("400x400")#x will be small
# add background color
r.configure(bg="grey")

#==============================
# add Label 

#-------> for roll no
rn=Label(r,text="Roll No ")
rn.place(x=20,y=20)

#-------> for First Name
fn=Label(r,text="First Name ")
fn.place(x=20,y=60)

#-------> for Last Name
ln=Label(r,text="Lasr Name ")
ln.place(x=20,y=100)

#-------> for EMail ID
en=Label(r,text="EMail ")
en.place(x=20,y=140)
#==============================
#Entry/Input Box in GUI 
# ----> for roll no
ern=Entry(r)
ern.place(x=160,y=20)

# ----> for First name
efn=Entry(r)
efn.place(x=160,y=60)
# ----> for Last Name
eln=Entry(r)
eln.place(x=160,y=100)
# ----> for roll no
een=Entry(r)
een.place(x=160,y=140)

#==============================
#add Button

b1=Button(r,text="Insert  ",bg="white")
b1.place(x=20,y=200)

b2=Button(r,text="Delete  ",bg="green")
b2.place(x=90,y=200)

b3=Button(r,text="Update  ",bg="orange")
b3.place(x=190,y=200)

b4=Button(r,text="Cancel  ",bg="red")
b4.place(x=250,y=200)


mainloop()


# from turtle import *
# speed(0)
# bgcolor("green")
# title("krishna")
# pencolor("white")

# for i in range(5000):
#     rt(i)
#     circle(120,i)
#     fd(i)
#     rt(90)
# done()