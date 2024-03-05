class Movie:
    def __init__(self,title,rating):
        self.title = title
        # below is a non-public attribute
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating.")

# Example
movie = Movie("Movie", 3.5)

print(movie.rating)  

movie.rating = 4.7 
print(movie.rating)  

movie.rating = 6.0  
print(movie.rating)  