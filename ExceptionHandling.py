# try:
#     a=int(input("enter the value of a: "))
#     print('A: ',a)
# except Exception as e:
#     print("Error Caught : ",e)
# print("Bye")


#multiple exception

# try:
#     print(x)
# except NameError:
#     print("variable Not define")
# except :
#     print("Exception Occur ")

# with else

# try:
#     # print("Hello world")
#     print(x)
# except:
#     print("SOmething went wrong")
# else:
#     print("Noting went wrong")
# print("Bye")


# finally block

# try:
#     a=int(input("enter a Number "))
#     print('A :',a)
# except :
#     print('Error Caught ')
# finally:
#     print('Done')


# user define exception

# class MyEx(Exception): #inherit the exception Classs
#     pass
# a=int(input("Enter a Interger value"))

# if a>5:
#     raise MyEx("Some went wrong Krishna")
# else:
#     print("greate")