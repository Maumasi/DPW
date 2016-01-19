from hotelView import Page
from hotelModel import *

class MyApp(object):
    def __init__(self, app):
        # app.response.write('My app')
        print "MyApp started"

        p = Page()
        p.title = "Beer"
        # html = p.print_out()
        # app.response.write(html)
        # print app.request.GET["user"]

        if app.request.GET:
            # self.user = app.request.GET["user"]
            app.response.write(p.form_exists())
        else:
            p.print_out()
            app.response.write(p.print_out())
