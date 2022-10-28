class A:
    def __init__(self):
        print('Calsss A inherit')
class B(A):
    def __init__(self):
        super().__init__()
        print("class B inherit")
b=B()
'''
Calsss A inherit
class B inherit

'''