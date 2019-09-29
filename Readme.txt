506 Final Project Readme Template

1. Describe your project in 1-4 sentences. Include the basic summary of what it does, and the output that it should generate/how one can use the output and/or what question the output answers. 
My project gathers data about movies that are now playing in theaters from the movie database api ('http://api.themoviedb.org/3/movie/now_playing?api_key=a9318d1cc2a93a4f7bede01fde6d1f68') and then inputs these movies individually into the omdb api and returns information about the movies. This information includes the title of the movie, the plot, the imdbRating, the Awards and more. Then the program uses the imdbRating to decide whether or not the movie is worth watching. Then it collects data from mapquest as well to direct an individual to their closest movie theater. 
it collects information about the closest movie theater and then gives you directions to the movie theater by using mapquest. 
2. Explain exactly what needs to be done to run your program (what file to run, anything the user needs to input, anything else) and what we should see once it is done running (should it have created a new text file or CSV? What should it basically look like?).
First run try2.py
then when asked to input an address, do this: 

To run the program, the user needs to input a starting address in Ann Arbor. For the purpose of running this program on cached data please 105 s state street ann arbor mi 48109. Please do not put a space because the prompt that asks you to input data and the data you input. 
Please download all the cached files. 

It will print out some recommendations for films that are now playing, whether or not it is worth seeing. It will also print the plot, title, imdb rating and awards of each movie. Then it will 
(Your program running should depend on cached data, but OK to write a program that would make more sense to run on live data and tell us to e.g. use a sample value in order to run it on cached data.)

EXAMPLE:
First run python myproject.py
Then, when it asks for a 3-letter airport code, type an airport abbreviation. You should type "DTW" to use the cached data.
You should have a new file in your directory afterward called airport_info.csv which contains... <explain further>
etc.

3. List all the files you are turning in, with a brief description of each one. (At minimum, there should be 1 Python file, 1 file containing cached data, and the README file, but if your project requires others, that is fine as well! Just make sure you have submitted them all.)

try2.py
omdb_cached_results.txt
quest_cached_results.txt
mapquest_cached_results.txt
tmdb_cached_fname.txt

4. Any Python packages/modules that must be installed in order to run your project (e.g. requests, or requests_oauthlib, or...):
import json, requests
import requests_oauthlib
import webbrowser
import json
import requests
import pickle
import unittest

5. What API sources did you use? Provide links here and any other description necessary.
https://www.themoviedb.org/documentation/api
https://www.omdbapi.com/
https://developer.mapquest.com/

6. Approximate line numbers in Python file to find the following mechanics requirements (this is so we can grade your code!):
- Sorting with a key function: line 62
- Use of list comprehension OR map OR filter: line 61 
- Class definition beginning 1: line 68
- Class definition beginning 2: line 241
- Creating instance of one class: 69
- Creating instance of a second class: 242
- Calling any method on any class instance (list all approx line numbers where this happens, or line numbers where there is a chunk of code in which a bunch of methods are invoked): 270
- (If applicable) Beginnings of function definitions outside classes: 63, 160
- Beginning of code that handles data caching/using cached data:
- Test cases: 283

8. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?
I did this project because I never really watch tv, so I usually do not know what movies are in theaters. So having this tool would be really helpful to figure out what movies are good. Also I am terrible with directions so it is nice to know what theatres are by me and how to get there. 