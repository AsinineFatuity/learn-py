class Movie:
    def __init__(self,movie_name,movie_director) -> None:
        self.name = movie_name
        self.director = movie_director
    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")
my_movie = Movie('The Matrix','Wachowski')
my_movie.print_info()
