# # sum=0
# # n=int(input("enter value "))
# # while n>0:
# #     sum=sum+n
# #     n-=1
# #     print("sum : ",sum)
# # sum=0
# # n=int(input("enter value "))
# # while n>0:
# #     sum=sum+n
# #     n-=1
# #     print("sum : ",sum)
# # else:
# #     print("Not done with",n)

# # for loops

# word=["react js ","angular","java  ","ruby rails"]

# # print(word)

# # for i in word:
# #     print(i)

# # with length calculation
# # for i in word:
# #     print(i," => ",len(i))



# '''
# *
# * *
# * * *
# * * * *
# * * * * *

# '''

# # for i in range(0,6,1):
# #     for j in range(0,i,1):
# #         print("*",end="")
# #     print()



# # '''
# # * * * * * 
# # * * * *
# # * * * 
# # * * 
# # *


# # '''
# # for i in range(6,0,-1):
# #     for j in range(i,0,-1):
# #         print(" * ",end="")
# #     print()

# for i in range(0,5,1):
#     for j in range(0,i,1):
#         print(str(i)+str(j)+" ",end="")
#     print()
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(str(i)+str(j)+" ",end="")
#     print()


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(str(i)+str(j)+" ",end="")
    print()

