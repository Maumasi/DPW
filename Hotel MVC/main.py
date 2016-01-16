from hotelController import *

class ReservationApp(object):
    def __init__(self):
        # print "ReservationApp created"

        # make an instance of the Controller
        self.__hotel_controller = HotelController()

    # Method for user to choose between logging in or making a new reservation
    def intro(self):
        return self.__hotel_controller.intro()

r = ReservationApp()
r.intro()