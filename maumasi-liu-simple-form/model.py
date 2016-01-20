
class Model(object): # Controller
    def __init__(self, app):
        # app.response.write('My app')
        print "model started"

        self.__app = app
        self.user_input = []
        self.user = [{}]

        self.user_input = self.__app.request.GET
        self.user[0]["user"] = self.user_input["user"]
        self.user[0]["movie"] = self.user_input["movie"]
        # self.user[0][]


        self.html = app.response.write()
        print self.user

    #
    # def html(self,el):
    #     return self.__app.response.write(el)
    #
