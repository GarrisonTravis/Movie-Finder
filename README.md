# Movie-Finder

This repository contains the Python code for my Movie Finder & Recommendations program. After running the program, you will be presented with these choices:
```
 1. Movie Credits
 2. TV Credits
 3. Movie Suggestions
 4. TV Suggestions
 ```
 Options 1 and 2 will prompt you to enter the name of a actor/actress and will give you all the movies/tv shows that they have appeared in. Options 3 and 4 will prompt you to enter a movie/tv show and will give you recommendations that are similar.
 
 The Movie Database (TMDB) API was used to generate the results.

# To Run:
```
python MovieFinder.py
```
You will need the HTTP library requests to run successfully. To install with pip run:
```
pip install requests
```
Or you can use the requirements.txt file after creating a virtual environment:
```
pip install -r requirements.txt
```
