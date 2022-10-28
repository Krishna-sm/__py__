# single Inheritence
# class A:#parent class
#     def P(self):#parent class Property
#         print("Class A is Called ")
# class B(A):#Child  class which inhrit class A
#     def P2(self):#Child class Property
#         print("Class B is Called ")

# a=B()
# a.P()
# a.P2()

# Class A is Called 
# Class B is Called 

# Multilevel Inheritence

# class A: #parent class
#     def myFun(self):
#         print("Hello A")
# class B(A): # sub class which inherit the parent class
#     def myFun2(self):
#         print("Hello B")
# class C(B): #child class which inherit the sub parent class
#     def myFun3(self):
#         print("Hello C")

# #creating a Object of child class
# c=C()
# c.myFun()
# c.myFun2()
# c.myFun3()

# # output:
# Hello A
# Hello B
# Hello C

# #mulitiple inheritence
# class A:
#     def myFun(self):
#         print("Hello A ")
# class B:
#     def myFun2(self):
#         print("Hello B")
# class C(A,B):
#     def myFun3(self):
#             print("Hello C")
# # creating a object of class C
# c=C()
# c.myFun()
# c.myFun2()
# c.myFun3()
'''
Hello A 
Hello B
Hello C
'''

#herarical inhertence

# class A:
#     def myfun(self):
#         print("hello Class A ")
# class B(A):
#     def myfun2(self):
#         print("Hello Class B ")
# class C(A):
#     def myfun3(self):
#         print("Hello Class C ")

# #creating a Objects of B and C
# b=B()
# c=C()

# b.myfun()
# b.myfun2()

# c.myfun()
# c.myfun3()

# hello Class A 
# Hello Class B
# hello Class A
# Hello Class C

#hybrid Inhitence

# class A:
#     def myfun1(self) :
#         print("hello A")
# class B(A):
#     def myfun2(self) :
#         print("hello B")
# class C(A):
#     def myfun3(self) :
#         print("hello C")
# class D(B,C):
#     def myfun4(self) :
#         print("hello D")

# #creating a object
# d=D()
# d.myfun1()
# d.myfun2()
# d.myfun3()
# d.myfun4()

# hello A
# hello B
# hello C
# hello D
    
#super keyword

# class A:
#     def inputf(self):
#         print("Hello")
# class B(A):
#     def id(self):
#         super().inputf()
#         print("hello g")
# c=B()
# c.id()

# Hello
# hello g
# PS E:\python\index\__py__>