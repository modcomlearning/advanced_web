# Object Oriented Way
# Improves code re use
# think of an object - Car
# A car has attributes/state/properties   =  color, weight, height, age, size, name
# A car has behaviors/functions - what it does. move(), carry(), hoot()

# lets understand it.
# a class is where the object lives - blueprint/template
class Car:

    def __init__(self):
        self.name = 'Nissan'
        self.weight =  500
        self.color = 'blue'
        self.age = 10
        self.mileage = 50000
        # above we define attributes of a car as variables



    def move(self):  # behavior/function
        print('A car is moving')
        print('The car weight is ', self.weight)
        print('The car mileage is ', self.mileage)


    









