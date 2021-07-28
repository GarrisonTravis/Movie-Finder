import requests
import json

class Actor:
	def __init__(self, actor_name, actor_id):
		self.name = actor_name
		self.id = actor_id
		self.movies = []
		self.tv = []

	def print_movies(self):
		print()
		for movie in self.movies:
			print("{} ({})".format(movie.title, movie.date))

	def print_tv(self):
		print()
		for tv in self.tv:
			print("{} ({})".format(tv.title, tv.date))

	def sort_movies(self):
		self.movies.sort(reverse=True, key=lambda x: x.date)

	def sort_tv(self):
		self.tv.sort(reverse=True, key=lambda x: x.date)

class Movie:
	def __init__(self, movie_title, movie_date, movie_rating, movie_overview):
		self.title = movie_title
		self.date = movie_date
		self.rating = movie_rating
		self.overview = movie_overview

class TV:
	def __init__(self, tv_title, tv_date, tv_rating, tv_overview):
		self.title = tv_title
		self.date = tv_date
		self.rating = tv_rating
		self.overview = tv_overview


#Function to get an actor's id
def get_actor_id(actor_name):
	actor_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US", "query" : actor_name, "page" : "1", "include_adult" : "false"}

	response = requests.get("https://api.themoviedb.org/3/search/person", actor_params)

	results = response.json()["results"]
	#actor_data = json.dumps(results, sort_keys=True, indent=4)
	#print(actor_data)

	actor_id = results[0]["id"]
	#print(actor_id)
	return actor_id


#Function to get an actor's movie credits
def get_movie_credits(actor):
	movie_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US"}

	response = requests.get("https://api.themoviedb.org/3/person/{}/movie_credits".format(actor.id), movie_params)

	results = response.json()["cast"]
	#movie_data = json.dumps(results, sort_keys=True, indent=4)
	#print(movie_data)

	for movie in results:
		#Check if release_date is in the movie dictionary
		if "release_date" in movie.keys():
			#Check if release_date is present but empty
			if not movie["release_date"]:
				movie["release_date"] = "ND"
			actor.movies.append(Movie(movie["title"], movie["release_date"][0:4], movie["vote_average"], movie["overview"]))


#Function to get an actor's tv credits
def get_tv_credits(actor):
	tv_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US"}

	response = requests.get("https://api.themoviedb.org/3/person/{}/tv_credits".format(actor.id), tv_params)

	results = response.json()["cast"]
	#movie_data = json.dumps(results, sort_keys=True, indent=4)
	#print(movie_data)

	for tv in results:
		if "first_air_date" in tv.keys():
			if not tv["first_air_date"]:
				tv["first_air_date"] = "ND"
			actor.tv.append(TV(tv["name"], tv["first_air_date"][0:4], tv["vote_average"], tv["overview"]))


#Function to get a movie's id
def get_movie_id(base_movie):
	movie_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US", "query" : base_movie, "page" : "1", "include_adult" : "false"}

	response = requests.get("https://api.themoviedb.org/3/search/movie", movie_params)

	results = response.json()["results"]

	movie_id = results[0]["id"]
	
	return movie_id


#Function to get similar movies
def get_movie_suggestions(movie_id):
	sugg_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US", "page" : "1"}

	response = requests.get("https://api.themoviedb.org/3/movie/{}/similar".format(movie_id), sugg_params)

	results = response.json()["results"]

	for movie in results:
		print(movie["title"])

def main():
	print(" 1. Movie Credits")
	print(" 2. TV Credits")
	print(" 3. Movie Suggestions")
	print(" 4. TV Suggestions\n")
	sel = input("Select an option: ")

	if sel == "1":
		actor_name = input("Enter actor's name: ")
		actor_id = get_actor_id(actor_name)

		#Create an Actor object
		actor = Actor(actor_name, actor_id)

		get_movie_credits(actor)
		actor.sort_movies()
		actor.print_movies()

	elif sel == "2":
		actor_name = input("Enter actor's name: ")
		actor_id = get_actor_id(actor_name)

		#Create an Actor object
		actor = Actor(actor_name, actor_id)

		get_tv_credits(actor)
		actor.sort_tv()
		actor.print_tv()

	elif sel == "3":
		base_movie = input("Enter movie: ")
		movie_id = get_movie_id(base_movie) 
		get_movie_suggestions(movie_id)

	elif sel == "4":
		base_tv = input("Enter tv show: ")

	else:
		print("Invalid selection! Try again.\n")
		main()

if __name__ == "__main__":
    main()