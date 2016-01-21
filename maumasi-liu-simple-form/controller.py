from view import Body
from model import *

class Controller(object): # Controller
    def __init__(self, app):
        # app.response.write('My app')
        # print "controller started"

        self.author = {}

        view = Body()

        view.title = "Game Reviews"

        if app.request.GET:
            self.author["author"] = app.request.GET["author"]
            self.author["title"] = app.request.GET["title"]
            self.author["review"] = app.request.GET["review"]
            self.author["genre"] = app.request.GET["genre"]
            self.author["date"] = app.request.GET["date"]

            view.body = view.result(self.author)
            app.response.write(view.html())

        else:

            print self.author
            view.html()
            view.body = view.form
            app.response.write(view.html())



