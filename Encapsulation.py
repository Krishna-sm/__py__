#----> Encapsulation Achive By private
# class A:
#     def __init__(self,a):
#         self.__a=a
#         print("the value of ",self.__a)
# class B(A):
#     def __init__(self, b):
#         super().__init__(b)
#     def show(self):
#         print(self.__a)

# b=B(10)
# b.show()

#----> Encapsulation Achive By Protected

# class A:
#     def __init__(self,a):
#         self._a=a
#     def show(self):
#         print("The Protected variable of a class : ",self._a)
# class B(A):
#     def __init__(self, b):
#         super().__init__(b)
#     def show2(self):
#         print("Access The Protected variable  : ",self._a)
# b=B(10)
# b.show()
# b.show2()

'''
The Protected variable of a class :  10
Access The Protected variable  :  10

'''