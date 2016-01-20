from view import Body
from model import *

class Controller(object): # Controller
    def __init__(self, app):
        # app.response.write('My app')
        print "controller started"

        self.user = {}

        view = Body()
        # model = Model()

        view.title = "Beer"

        if app.request.GET:
            self.user["user"] = app.request.GET["user"]
            self.user["movie"] = app.request.GET["movie"]

            view.body = view.result(self.user[0]["user"])
            app.response.write(view.html())

        else:
            view.html()
            view.body = view.form
            app.response.write(view.html())

