from hotelModel import *
from hotelView import *

# # ------------------------------- Conteroller
class HotelController(object):
    def __init__(self):
        # print "HotelGest created"

        # instantiate  Model
        self.__model = HotelModel()

        # instantiate  View
        self.__view = HotelView()

# Privet method for logging in
    def __login(self):
        # user {name : "", password : ""}
        user = self.__view.login_user()

        # test if there is a match. returns a boolean
        logged_in = self.__model.user_match(user)

        if logged_in:
            # show user data after login
            self.__view.analyse_data(self.__model.get_data(user))

        else:
            # loops until user is logged in or gives up
            while not logged_in:

                if logged_in:
                    self.__view.analyse_data(self.__model.get_data(user))

                else:
                    logged_in = self.__view.retry_login()

                    if not logged_in:
                        # stop loop if user types n or N
                        break

                    else:
                        # test if there is a match again. returns a boolean
                        logged_in = self.__view.analyse_data(self.__model.get_data(logged_in))

# Privet method for making a new reservation
    def __make_reservation(self):
        reservation = self.__view.new_reservation()
        self.__model.set_new_reservation(reservation)
        self.__view.analyse_data(reservation)

# Method for asking the user to login or make a anew reservation
    def intro(self):
        answer = self.__view.intro_prompt()

        if answer == "new":
            self.__make_reservation()

        else:
            self.__login()


