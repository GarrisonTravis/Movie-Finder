import requests
import json

def get_actor_id(actor_name):
	actor_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US", "query" : actor_name, "page" : "1", "include_adult" : "false"}

	response = requests.get("https://api.themoviedb.org/3/search/person", actor_params)

	results = response.json()["results"]
	#actor_data = json.dumps(results, sort_keys=True, indent=4)
	#print(actor_data)

	actor_id = results[0]["id"]
	#print(actor_id)
	return actor_id

def get_movie_credits(actor_id):
	movie_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US"}

	response = requests.get("https://api.themoviedb.org/3/person/{}/movie_credits".format(actor_id), movie_params)

	results = response.json()["cast"]
	#movie_data = json.dumps(results, sort_keys=True, indent=4)
	#print(movie_data)

	print()
	for movie in results:
		print(movie["original_title"])
		print()

def get_tv_credits(actor_id):
	tv_params = {"api_key" : "5ef5cb1f27635cdee648c0217464880f", "language" : "en-US"}

	response = requests.get("https://api.themoviedb.org/3/person/{}/tv_credits".format(actor_id), tv_params)

	results = response.json()["cast"]
	#movie_data = json.dumps(results, sort_keys=True, indent=4)
	#print(movie_data)

	print()
	for tv in results:
		print(tv["name"])
		print()


def main():
	print(" 1. Movie Finder")
	print(" 2. TV Finder\n")
	sel = input("Select an option: ")

	if sel == "1":
		actor_name = input("Enter actor's name: ")
		actor_id = get_actor_id(actor_name)
		get_movie_credits(actor_id)
	elif sel == "2":
		actor_name = input("Enter actor's name: ")
		actor_id = get_actor_id(actor_name)
		get_tv_credits(actor_id)
	else:
		print("Invalid selection! Try again.\n")
		main()

main()