from view import Body

class Controller(object): # Controller
    def __init__(self, app):
        # app.response.write('My app')
        print "MyApp started"

        self.user = [{}]

        # p = Page()
        b = Body()

        b.title = "Beer"
        # html = p.print_out()
        # app.response.write(html)
        # print app.request.GET["user"]

        if app.request.GET:
            self.user[0]["user"] = app.request.GET["user"]
            self.user[0]["movie"] = app.request.GET["movie"]

            b.body = b.html_complile(self.user[0]["user"])
            app.response.write(b.html())

        else:
            b.html()
            b.body = b.form
            app.response.write(b.html())

