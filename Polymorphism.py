# there are two type of polymorphism

# run time Polymorphism
#----> Method Overloading
# Compile time Polymorphism
#----> Method Overriding

# #method Overlading 
# class A:
#     def fun(self):
#         print("function has no Argument ")
#     def fun(self,a):
#         print("function has 1 Argument ")
#     def fun(self,a,b):
#         print("function has 2 Argument ")
# # create a object
# a=A()
# a.fun()

# TypeError: A.fun() missing 2 required positional arguments: 'a' and 'b'

# ---------> it can not support Run time Polymorphism

# method Overriding 
'''
class A:
    def fun(self):
        print("Class A function Called ")
class B(A):
    def fun(self):
        print("Class B function Called ")
class C(A):
    def fun(self):
        print("Class C function Called ")

a=C()
a.fun()#Class C function Called 

'''
