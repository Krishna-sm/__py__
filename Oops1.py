#Creating a Class
# class MyClass:
#     x=5 # property of class
# print(x) # name 'x' is not defined


#  creating a Object
# class MyClass:
#     x=5
# m=MyClass()
# print(m.x) #5

#create a function with oops

# class MyClass:
#     def fun():
#         print("Hello")
# m=MyClass()
# m.fun()
# #TypeError: MyClass.fun() takes 0 positional arguments but 1 was given

# so .
# class Myclass:
#     def fun(self):
#         print("Hello")
# m=Myclass()
# m.fun() #Hello

#creating a constructor

# class Myclass:
#     def __init__(self):
#         print("Hello world")
# m=Myclass() #Hello world


#pass values in function
# class Myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def out(self):
#         print("Your Name is : ",self.name)
#         print("Your Name is : ",self.age)

# # creating a object
# m=Myclass("Krishna",18)
# m.out()
'''
Your Name is :  Krishna
Your Name is :  18
'''
# access the variable with object using 
# print(m.age) #18
# print(m.name)#Krishna

#change the value using object

# print("Before update ",m.age)
# m.age=89
# print("After update ",m.age)
# Before update  18
# After update  89
# delete object
# del m

# print(m.age)
# #name 'm' is not defined

# del m.age
# print(m.age) # myclass has no attribute

class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def out(self):
        print("your name is :",self.name)
        print("your age is :",self.age)
    
m=MyClass("Krishna",18)
m.out()
m.age=45
m.out()

