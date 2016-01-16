import random

# # ------------------------------- View
class HotelView(object):
    def __init__(self):
        # print "HotelRoom created"

        self.__logged_in = False

# Private method in used only in this class
    def __get_data(self, data):

        print "\nWelcom " + data["user"] + "! Here is your reservation with us:\n" \
                    "Reservation Date: " + data["reservation_date"] +"\n" \
                    "Nights reserved: " + str(data["nights_reserved"]) + "\n" \
                    "Room: " + data["room_number"] + "\n" \
                    "\nCard on file:\n " \
                    "   Type: " + data["credit_card"]["card_type"] + "\n " \
                    "   Card Number: " + str(data["credit_card"]["card_number"]) + "\n " \


    def login_user(self):
        print "\n---- Login -----"
        return {"user" : raw_input("\nEnter name:\n"), "password" : raw_input("Enter password:\n")}

# prints data to screen if there is any data to print
    def analyse_data(self, data):

        if isinstance(data,dict):
            self.__logged_in = True
            self.__get_data(data)
            return self.__logged_in

        else:
            self.__logged_in = False
            return self.__logged_in

# used for wrong name entry
    def retry_login(self):
        print "\nUser name or password did not match" \
              "\nwhat we have on file\n"

        answered  = False
        while not answered:
            retry = raw_input("Do you want to try another name? Y/N \n")

            if (retry == "Y") or (retry == "y"):
                name = {"user" : raw_input("\nEnter name:\n"), "password" : raw_input("Enter password:\n")}
                answered = True
                return name

            elif (retry == "N") or (retry == "n"):
                print "Good Bye."
                answered = True
                return False

            else:
                print "\nYou didn't type: \"Y\" or \"N\""


    def new_reservation(self):
        user = {}
        print "\n---- Make a new reservation -----"
        user["user"] = raw_input("\nEnter your name:\n")
        user["password"] = raw_input("\nMake a password:\n")
        user["reservation_date"] = raw_input("\nDate for reservation [MM/DD/YYYY]:\n")
        user["nights_reserved"] = raw_input("\nTotal nights visiting:\n")
        user["room_number"] = str(random.randint(0, 5)) + str(random.randint(0, 30))
        user["credit_card"] = {"card_type" : raw_input("\nEnter your credit card type:\n"), "card_number" : raw_input("\nEnter your credit card number:\n")}
        return user

    def intro_prompt(self):

        answered = False
        while not answered:

            print "\nAre you logging in or making a new reservation?"

            answer =  raw_input(" * Login type [login] \n"
                                " * Make a new reservation type [new]\n")


            if answer == "login":
                answered = True
                return "login"

            elif answer == "new":
                answered = True
                return "new"

            else:
                print "\nPlease type [login] or [new]\n"


