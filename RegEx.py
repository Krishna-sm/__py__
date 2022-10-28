# from re import *

# pattern=r"^abc"
# string="abcdfed"
# print(match(pattern,string))
#----------> it check begining 
# if you want ot check the position 
# so you do wihew x.start() to postion-1


# search funtion

# import re
# print(re.search("k","hello krishna"))
# print("first whitespace start with : ",re.search("\s","helo krishna").start())


# # reaplce function in RegEx
# # import re


# Replace string with sub
# import re

# str1="i am from Rajiv "
# print("before Replace : ",str1)
# result=re.sub("Rajiv","rajiv",str1)
# print("After replace : ",result)


# replace characters
import re

str="I Am Krishna 8978"
print("Before Update: ",str)
print(re.sub(r"[a-z,A-Z]",r"^[A-Z]",str))