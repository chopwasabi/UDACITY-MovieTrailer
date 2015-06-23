import webbrowser
# Module for Displaying HTML File in Browser


class Movie():

    def __init__(self, movie_title, release_year,
                 movie_storyline, poster_image, trailer_youtube):
        """
                Initialize self(Local Variable) with the provided paramaters.
        """
        self.title = movie_title
        self.release_year = release_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Open up browser with the url of the movie trailer using the
        # Webbrowser module.
        webbrowser.open(self.trailer_youtube_url)
    # End of Movie Class
