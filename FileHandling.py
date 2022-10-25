
# # create a file
# # s="This is File Tutorial "
# # file=open("file/file.txt","w")
# # file.write(s)
# # print("File Created successFully")
# # file.close()


# #read the File Content 
# # file=open("file/file.txt","r")
# # s=file.read()
# # print(s)
# # file.close()


# #store List file 
# # l=["python "," Java "," Anuglar "," Php "]
# # file=open("file/list.txt","w")
# # file.writelines(l)
# # print("List Stored ")
# # file.close()

# #access the list from file
# # file=open("file/list.txt","r")
# # l=file.readlines()
# # print(l)
# # file.close()

# # from linecache import getline

# # file=open("file/list.txt","r")
# # l=getline(file,1)
# # print(l)
# # file.close()

# # os.rmdir('file')
# # print('folder delted')

from os import *
if path.exists('file/file.txt'):
    remove('file/file.txt')
    print('file deleted')
else:
    print("file not exist")

# #  
# import os
# os.remove('file.txt')
# print('file delted')



