from tkinter import *
import tkinter.messagebox as msg

def click():
    n=0
    n+=1
    msg.showinfo("clicked","hlo ")
r=Tk()
r.geometry("500x500")
r.title("app")
r.configure(bg="white")

bt=Button(r,text="clicked me",foreground="black",command=click)
bt.pack(padx="50",pady="90")
mainloop()