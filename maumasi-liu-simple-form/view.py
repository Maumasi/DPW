
class Page(object): # View
    def __init__(self):
        # print "view started"

        self.title = "Gamer Rants - Rant Form"
        self.css = "css/form.css"
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

        self.title = "Gamer Rants - " + title + " Review"
        self.css = "css/blog.css"
        self.js = ""

        blog = '''
        <section>
            <p id="bread-crumbs">Games  &rang;  Reviews  &rang;  {genre}  &rang;  {title}</p>
            <article>
                <header>
                    <h1>{title} Review</h1>
                    <div id="publish">
                        <div id="gr-logo">GR</div>
                        <p><span id="author">By {author}</span> <span id="date">Published on {date}</span></p>
                    </div>
                </header>
                <div id="content">
                    <p id="review">{review}</p>
                </div>
                <footer>
                    <p><span>Gamer Rants</span> <span>All user generated content is property of Gamer Rants &reg; Inc.</span></p>
                </footer>
            </article>
        </section>
        '''
        return blog.format(**locals())



