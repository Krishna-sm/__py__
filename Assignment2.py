# # a=int(input("enter How many Element You want to enter"))
# # l1=[]
# # for i in range(a):
# #     ele=int(input(print("enter index ",i+1)))
# #     l1.append(ele)

# # print(l1)

# # [5, 25, 256, 145, 265]


# # l=[1,2,3,4,5,6]
# # l.remove(3)
# # print(l)


# # l=["Java","php",".Net","Anuglar"]
# # print("Currunt List : ",l)
# # # l[2]="Python"
# # l.insert(2,"Python")
# # print("Updated List : ",l)

# t=("python",1,2,3,"Java",'A','B')
# # for i in t:
# #     print(i)

# # print("Print value Between ",t[1:5])

# print("Last Value is ",t[-1])

# t=(1,2,3,4,5,6,7,8)
# print(len(t))


# t=("Krishna","kana","Kanhiya")
# l=list(t)
# print(l)

l1=[1,2,3,4,5]
l2=['A','B','C','D','E']
d={}

for i in range(0,len(l1)):
    d.update({l1[i]:l2[i]})
print(d)