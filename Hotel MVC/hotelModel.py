
# # ------------------------------- Model
class HotelModel(object):
    def __init__(self):
        # print "HotelKeyCard created"


        self.__logged_in = False
        self.__guest = [{"user" : "Sam", "password" : "1234"}]

        # user's private data
        self.__data = {
            "Sam" : {
                "user" : "Sam",
                "password" : "1234",
                "nights_reserved" : "3",
                "room_number" : "520",
                "reservation_date" : "01/31/2016",
                "credit_card" : {
                    "card_type" : "Visa",
                    "card_number" : "1234-5678-1234-5678"
                } # credit_card
            } # Sam
        } # self.__data


    # loops to check for name matches
    def get_data(self, user): # Working

        for i in range(len(self.__guest)):

            if (user["user"] == self.__guest[i]["user"]) and (user["password"] == self.__guest[i]["password"]):
                return self.__data[user["user"]]

            else:
                return False

    # returns a boolean
    def user_match(self,name):

        while not self.__logged_in:

            for i in range(len(self.__guest)):

                if name == self.__guest[i]:
                    self.__logged_in = True
                    return True

                else:
                    return False

    def set_new_reservation(self, reservation):

        user = {"user" : reservation["user"], "password" : reservation["password"]}
        self.__guest.append(user)
        self.__data[user["user"]] = reservation

    def return_data(self):
      return self.__data

