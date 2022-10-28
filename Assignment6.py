# create a vechical class and call method by using class and Object

# class Vechical:
#     def car(self):
#         print("Its my car ")
# c=Vechical()
# c.car()
# Its my car 


# class Vechical:
#     def car(self):
#         pass
# c=Vechical()
# c.car()



# class Vechical:
#     def car(self):
#         print("fourtunre")
#     def car(self,a):
#         print("B|^| W")
# c=Vechical()
# c.car()
# c.car(10)
'''
class Vechical:
    def Car(self):
        print("It's My Car ")
    def Bike(self):
        print("it's My Bike ")
    def Cycle(self):
        print("it's My Cycle ")
class Bus(Vechical):
    def __init__(self):
        super().Car()
        super().Bike()
        super().Cycle()
    def show(self):
        print("This is My Bus")
b=Bus()
b.show()

'''

class Vechical:
    def Name(self):
        pass
class Bus(Vechical):
    def Name(self):
        print("it's Bus ")
class Bike(Vechical):
    def Name(self):
        print("it's Bike")
class Car(Vechical):
    def Name(self):
        print('its Car')

# creating objects
bus=Bus()
bike=Bike()
car=Car()
#calling  functions

bus.Name()
bike.Name()
car.Name()