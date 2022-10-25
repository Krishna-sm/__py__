def generateFIle(d):
    file=open('emp.txt','w')
    file.write(str(d))
    print("Data save SuccessFully...")
    file.close()
def inDict(num):
    for i in range(num):
        d.update({l1[i]:l2[i]})
    print(d)

print("""
        ============ Welcome To Krishna World ============
""")

num=int(input("enter how many record you want to store"))
l1=[]
l2=[]
d={}
for i in range(num):
    print("enter name for  ",(i+1)," Employee")
    name=input()
    print("enter Age for  ",(i+1)," Employee")
    age=int(input())
    l1.append(name)
    l2.append(age)

inDict(num)
generateFIle(d)



