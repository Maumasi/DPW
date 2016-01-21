
class Page(object): # View
    def __init__(self):
        print "view started"

        self.title = "TGB - Review Form"
        self.css = "css/main.css"
        self.js = "js/app.js"
        self.body = ""

        self.__html = '''
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
        <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>

        <link href= "{self.css}" rel= "stylesheet"/>
        <script type="text/javascript" src="{self.js}"></script>
        <title>{self.title}</title>
    </head>
    <body>
        <nav>
            <h1>Gamer Rants</h1>
            <p><a target="_blank" href="https://www.e3expo.com" >Look for us at <span>E3 2016</span></a></p>
        </nav>


        {self.body}
        <script type="text/javascript" src="{self.js}"></script>
    </body>
</html>
        '''

    def html(self):
        return self.__html.format(**locals())


class Body(Page):
    def __init__(self):
        super(Body, self).__init__()


        self.form = '''
        <div id="form-hero">
            <form method="GET">
                <h2>Tell us your <strong>Rant</strong></h2>
                <input type="text" placeholder="Author Name (Yours)" name="author" required="required">
                <input type="text" placeholder="Date" id="date" name="date" required>
                <input type="text" placeholder="Game Title" name="title" required>
                <select required name="genre">
                    <option value="Miscellaneous">Game Genre</option>
                    <option value="Shooter">Shooter</option>
                    <option value="RPG">RPG</option>
                    <option value="Fantasy">Fantasy</option>
                    <option value="Casual">Casual</option>
                    <option value="Fighter">Fighter</option>
                    <option value="Unique">Unique</option>
                </select>
                <textarea placeholder="Give us your thoughts." name="review"></textarea>
                <input type="submit" value="Submit" id="submit">
            </form>
        </div>
        '''

    def result(self,game):

        title = game["title"]
        author = game["author"]
        date = game["date"]
        review = game["review"]
        genre = game["genre"]

        self.title = title + " Review"

        blog = '''
        <section>
        <p>Games > Genre > {genre}
            <article>

                <h1>{title} Review<h1>

                <p><strong>By {author}</strong>
                on {date}</p>

                <p>{review}</p>
            </article>
        </section>
        '''
        return blog.format(**locals())



