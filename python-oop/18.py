class Movie:
	def __init__(self, title, director, rental_price, is_rented=False):
		self.title = title
		self.director = director
		self.rental_price = rental_price
		self.is_rented = is_rented

	def __str__(self):
		return f"{self.title}, directed by {self.director} \
- {'Rented' if self.is_rented else 'Available'} \
- Price: {self.rental_price}"

class Rental:
	def __init__(self, movies):
		self.movies = movies
		self.__total_income = 0
	
	def rent_movie(self, title):
		for movie in self.movies:
			if movie.title != title: continue

			if movie.is_rented:
				print( f"Sorry, '{title}' is already rented.")
				return
			
			movie.is_rented = True
			print( f"You have rented '{title}' for {movie.rental_price}.")
			self.__total_income += movie.rental_price
			return
		print( f"Movie '{title}' not found.")
	
	def return_movie(self, title):
		for movie in self.movies:
			if movie.title != title: continue

			if not movie.is_rented:
				print( f"'{title}' was not rented.")
				return
			
			movie.is_rented = False
			print( f"You have returned '{title}'.")
			return
		print( f"Movie '{title}' not found.")

	def get_rented_movies(self):
		return [movie for movie in self.movies if movie.is_rented]
	
	def get_total_income(self):
		return self.__total_income

movies = [
	Movie("Inception", "Christopher Nolan", 50_000),
	Movie("The Matrix", "The Wachowskis", 30_000),
	Movie("Interstellar", "Christopher Nolan", 70_000),
]
rental_service = Rental(movies)
rental_service.rent_movie("Inception")
rental_service.rent_movie("The Matrix")
rental_service.return_movie("Inception")
rental_service.rent_movie("Interstellar")
print("Rented Movies:")
for rented_movie in rental_service.get_rented_movies():
	print(rented_movie)
print("Total Income:", rental_service.get_total_income())