# Import random function and methods
import random

# Library() class used to make all calculations in Newton's 3rd Law experiment in main.py
class Library():
    def __init__(self):
        self.mass = 0
        self.acceleration = 0
        self.your_force = 0
        self.obj_force = 0
        self.your_area = 0
        self.obj_area = 0
        self.your_pressure = 0
        self.obj_pressure = 0
        self.pressure_dif = 0
        self.obj_vs = ""
        self.broke_through = True

# force method used for generating your_force value after user input
    def force(self):
        self.your_force = int(self.acceleration) * int(self.mass)


# pascals_principle method used for:
#     -generating obj name you're going up against
#     -generating obj_area
#     -generating obj_force
#     -generating obj_pressure
#     -generating your_pressure
#
# All of these except the obj's name are used to calculate
# the accurate pressure for you and the obj you're going up against
    def pascals_principle(self):

# the value of the keys are used for Library.obj_area to get
# a value for an object's area to calculate the object's force.
        obj_dic = {"Piano": 50, "Brick wall": 100, "Glass window": 2, "Stack of milk bottles": 3, "Panzer Tank": 1000}

# Turn all obj_dic's keys into elements in a list
        obj_list = obj_dic.keys()
        index = obj_list[random.randrange(0, len(obj_list))]

        self.obj_vs = index
        self.obj_area = obj_dic[index]
        self.obj_force = (int(self.your_force) * int(self.obj_area)) / int(self.your_area)

        self.obj_pressure = self.obj_force / int(self.your_area)
        self.your_pressure = int(self.your_force) / int(self.obj_area)

# winner method used to test if broke_through should be True or False
    def winner(self):

        if self.obj_pressure < self.your_pressure:
            self.pressure_dif = self.your_pressure - self.obj_pressure
            self.broke_through = True
        else:
            self.pressure_dif = self.obj_pressure - self.your_pressure
            self.broke_through = False
        return self.winner


# Printer() class used to print out messages based on results from user inputs
class Printer():
    def __init__(self):
        print "Printer created"

# greeting method used to explain what this app is attempting to do.
    def greeting(self):
        print "\nLet's put Newton's 3rd Law to the test. " \
              "\nDo objects exert equal and opposite forces when in contact with each other?" \
              "\nSound painful, It might be. Let's play!\n"
        return

# outcome method used to print out the outcome message to the user baes on their results
    def outcome(self,
                bool,
                obj_description,
                pressure_dif,
                obj_pressure,
                your_pressure):
# tie outcome
        if obj_pressure == your_pressure:
            print "\nOUTCOME:" \
                  "You almost made it through, " \
                  "\nbut it looks like you and the" + obj_description + " " \
                  "\nhad the same amount of pressure pushing back on each other."
# user win outcome
        elif bool:
            print "\nOUTCOME:" \
                  "\nYou broke through a " + obj_description + "! " \
                  "\nYou might need medical attention, but you did it!! " \
                  "\nYou had " + str(pressure_dif) + "Kg per sq/meter than the " + obj_description + "."
# user lose outcome
        else:
            print "\nOUTCOME:" \
                  "\nDang, looks like you need to go to the hospital. " \
                  "\nYou just ran into a " + obj_description + " as hard as you could, your a dumb, dummy. " \
                  "\nThe " + obj_description + " had " + str(pressure_dif) + "Kg per sq/meter more than you."

# summery method is used to print out a report of why the user mon or lost
    def summery(self,
                obj_description,
                obj_pressure,
                obj_force,
                your_force,
                your_pressure):
        print "\nSUMMERY:" \
              "\nYour Force: " + str(your_force) + " " + \
              "\n" + obj_description + "'s Force: " + str(obj_force) + " " \
              "\nYour total pressure: " + str(your_pressure) + " " + \
              "\n" + obj_description + "'s total pressure: " + str(obj_pressure)
