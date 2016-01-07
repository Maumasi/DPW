
from library import *

class MainHandler():
    def __init__(self):

        calc_results = Library()
        narrator = Printer()

# I used try/except to test if an integer was entered. If not then the user will be prompted again
        mass_is_int = True
        while mass_is_int:
            try:
                calc_results.mass = raw_input("Enter weight:\n")
                isinstance(int(calc_results.mass), int)

                print calc_results.mass

                mass_is_int = False
            except Exception:

                print "You didn't enter a number!"

                mass_is_int = True

# I used try/except to test if an integer was entered. If not then the user will be prompted again
        accel_is_int = True
        while accel_is_int:
            try:
                calc_results.acceleration = raw_input("Enter your max running speed in meters (in integers):\n")
                isinstance(int(calc_results.acceleration), int)

                print calc_results.acceleration

                accel_is_int = False
            except Exception:

                print "You didn't enter a number!"

                accel_is_int = True

# I used try/except to test if an integer was entered. If not then the user will be prompted again
        area_is_int = True
        while area_is_int:
            try:
                calc_results.your_area = raw_input("Enter your body's front surface area in square meters \n(as close as posible using integers)\n")
                isinstance(int(calc_results.your_area), int)

                print calc_results.your_area

                area_is_int = False
            except Exception:
                print "You didn't enter a number!"
                area_is_int = True


        if calc_results.winner:
            event_outcome.
            pass


        # print play.force()
        #
        # print
        # print play.obj_force
        # print play.your_force
        #
        # print play.pascals_principle()

play_it = MainHandler()


