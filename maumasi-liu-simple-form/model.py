
class Model(object): # Controller
    def __init__(self, app):
        # app.response.write('My app')
        print "model started"

        self.user = {}

        input = app.request.GET
        # self.user["user"] = input["user"]
        # self.user["movie"] = input["movie"]


        print self.user



    #
    # def html(self,el):
    #     return self.__app.response.write(el)
    #
