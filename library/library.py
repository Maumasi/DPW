import random

class Library():
    def __init__(self):
        print "Library created"
        self.mass = 0 #
        self.acceleration = 0 #
        self.your_force = 0 #
        self.obj_force = 0 #
        self.your_area = 0 #
        self.obj_area = 0 #
        self.your_pressure = 0
        self.obj_pressure = 0
        self.winner = True



    def force(self):
        self.your_force = int(self.acceleration) * int(self.mass)
        return self.your_force

    def pascals_principle(self):

# the value of the keys are used for Library.obj_area to get
# a value for an object's area to calculate the object's force.
        obj_dic = {"Piano": 6, "Brick wall": 10, "Paper poster": 2, "Stack of milk bottles": 3}
        obj_list = obj_dic.keys()
        index = obj_list[random.randrange(0, len(obj_list))]

        self.obj_area = obj_dic[index]
        self.obj_force = (int(self.your_force) * int(self.obj_area)) / int(self.your_area)
        return self.obj_force

    def winner(self):
        if self.obj_force < self.your_force:
            self.winner = True
        else:
            self.winner = False

        return self.winner



class Printer():
    def __init__(self):

        def greeting():
            print "\nLet's see what you can run through? \nSound painful, It might be. Let's play!"

        def outcome(bool, ):
            if bool:
                print "\nYou survived! You broke through!"
            else:
                print "\nDang, looks like you need to go to the hospital."








