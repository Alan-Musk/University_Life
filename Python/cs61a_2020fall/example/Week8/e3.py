# codes from Jade's Guide to Object Oriented Programming
class Car:
    num_wheels=4
    def __init__(self,color,make):
        self.color=color
        self.make=make
        self.gas=10
        print("New car on the road!")
    def drive(self):
        if self.gas==0:
            return "Can't drive on an empty tank!"
        self.gas-=5
        return 'vroom vroom'
    def park(self):
        if self.num_wheels>=4:
            return "In between the white lines!"
        else:
            return "Oof,you better find a new spot:("
    def paint(self):
        return "Added new"+self.color+" paint to the  "+self.make+"!"
    def refill_gas_tank(self):
        self.gas=10

class Motorcycle(Car):
    num_wheels=2