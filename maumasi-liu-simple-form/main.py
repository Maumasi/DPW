# ---------------------------
# <html>
#     <head>...</head>            ---> 1
#     <body>...
# ----------------------------
#     ... body content ...
#         ...                     ---> 2
#         ...
#  ---------------------------
#     </body>
# <html>                          ---> 3
# ------------------------------
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')
        print "MainHandler created"
        my_app = MyApp(self)


class MyApp(object): # Controller
    def __init__(self, app):
        # app.response.write('My app')
        print "MyApp started"

        self.user = {}

        # p = Page()
        b = Body()

        b.title = "Beer"
        # html = p.print_out()
        # app.response.write(html)
        # print app.request.GET["user"]

        if app.request.GET:
            self.user["user"] = app.request.GET["user"]

            b.body = b.hi_there(self.user["user"])
            app.response.write(b.html())

            print b.html

        else:
            b.html()
            b.body = b.form
            app.response.write(b.html())


class Page(object): # View
    def __init__(self):

        self.css = ""
        self.js = ""

        self.body = ""
        self.title = ""
        self.__html = '''
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

        <link href= "{self.css}" rel= "stylesheet"/>
        <script type="text/javascript" src="{self.js}"></script>
        <title>{self.title}</title>
    </head>
    <body>

        {self.body}
    </body>
</html>
        '''

    def html(self):  # Model
        return (self.__html).format(**locals())


class Body(Page):
    def __init__(self):
        super(Body, self).__init__()
        self.form = '''
        <h1>Liu's Form</h1>

        <form method="GET">
            <lable>Name<input type="text" placeholder="Name" name="user"></lable>
            <input type="submit" value="Submit">
        '''

    def hi_there(self,user):
        self.hi = '''<p>Hi {user}</p>'''
        return (self.hi).format(**locals())


#
# handlers:
# - url: /css
#   static_dir: css
#
# some things need to be excaped ex : \.
#
































app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
