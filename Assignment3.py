# def fun(name,subject):
#     print("Hello ",name," You subject is ",subject)

# fun("Krishna","BCA")
# fun("Kana","BBA")


# def sum(n):
#    if n<=1:
#     print(n)
#     return n
#    else:
#     print(n)
#     return n+sum(n-1)

# print(sum(8))



# x=lambda a,b:a+b
# print(x(5,10))

# from random import *
# str="Abcde"
# ''.join(sample(str,len(str)))
# print(str)


# otp=randint(1000,5000)
# print("the Otp is : ",otp)

from random import *


captch_list=['1A45DF','45De89w','Fr89de','89deQ56']

shuffle(captch_list)
print(captch_list)
print("Captcha is : ",choice(captch_list))






