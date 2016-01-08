# Import the whole libaray.py file
from library import *

class MainHandler():
    def __init__(self):

# instances of the classes: Library & Printer
        calc_results = Library()
        narrator = Printer()

# An introdution to what this app is about
        narrator.greeting()

# I used try/except to test if an integer was entered. If not then the user will be prompted again.
# the bool before the while loop is used to keep the loop active until the try condition is met.
        mass_is_int = True
        while mass_is_int:
            try:
                calc_results.mass = raw_input("Enter weight:\n")
                isinstance(int(calc_results.mass), int)

                mass_is_int = False
            except Exception:

                print "You didn't enter a number!"

                mass_is_int = True

# I used try/except to test if an integer was entered. If not then the user will be prompted again.
# the bool before the while loop is used to keep the loop active until the try condition is met.
        accel_is_int = True
        while accel_is_int:
            try:
                calc_results.acceleration = raw_input("Enter your max running speed in meters/second (in integers):\n")
                isinstance(int(calc_results.acceleration), int)

                accel_is_int = False
            except Exception:

                print "You didn't enter a number!"
                accel_is_int = True

# I used try/except to test if an integer was entered. If not then the user will be prompted again.
# the bool before the while loop is used to keep the loop active until the try condition is met.
        area_is_int = True
        while area_is_int:
            try:
                calc_results.your_area = raw_input("Enter your body's front surface area in square meters "
                                                   "\n(as close as posible using integers)\n")
                isinstance(int(calc_results.your_area), int)
                area_is_int = False
            except Exception:
                print "You didn't enter a number!"
                area_is_int = True

# Run all calulations after getting all the needed info
        calc_results.force()
        calc_results.pascals_principle()
        calc_results.winner()

# print out the outcome of the collision of the player and the object
        narrator.outcome(calc_results.broke_through,  # ...boolean fore breaking through obj
                         calc_results.obj_vs,  # ..........The obj name you ran up against
                         calc_results.pressure_dif,  # ....pressure difference bwteen you and obj
                         calc_results.obj_pressure,  # ....obj's total pressure
                         calc_results.your_pressure)  # ...your total pressure

        narrator.summery(calc_results.obj_vs,  # .........The obj name you ran up against
                         calc_results.obj_pressure,  # ...obj's total pressure
                         calc_results.obj_force,  # ......obj's total fore
                         calc_results.your_force,  # .....your total fore
                         calc_results.your_pressure)  # ..your total pressure

# Instantiate MainHandler() class
play_it = MainHandler()


