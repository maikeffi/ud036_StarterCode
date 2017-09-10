import webbrowser
class Trailer():

    #initiates the class Trailer and passes the needed parameters for the website
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #runs the youtube link on a browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
