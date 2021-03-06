import webbrowser

class Movie():
    '''This is a class for storing information about movies.'''
    def __init__(self, movie_title, movie_year, poster_image, trailer_youtube, movie_rating):
        self.title = movie_title
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
    def show_trailer(self):
        '''This method opens a youtube url.'''
        webbrowser.open(self.trailer_youtube_url)
