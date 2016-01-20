


class Page(object): # View
    def __init__(self):
        print "view started"

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

    def html(self):
        return self.__html.format(**locals())


class Body(Page):
    def __init__(self):
        super(Body, self).__init__()
        self.form = '''
        <h1>Liu's Form</h1>

        <form method="GET">
            <lable>Name<input type="text" placeholder="Name" name="user"></lable>
            <lable>Movie<input type="text" placeholder="Name" name="movie"></lable>
            <input type="submit" value="Submit">
        '''

    def html_complile(self,user):
        self.hi = '''<p>Hi {user}</p>'''
        return (self.hi).format(**locals())




