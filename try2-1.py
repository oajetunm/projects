import json, requests
import requests_oauthlib
import webbrowser
import json
import requests
import pickle
import unittest
#import

addy = raw_input("please enter an address in Ann Arbor")
s = addy.split(" ")
j = "+"
address = j.join(s)

def canonical_order(d):
    alphabetized_keys = sorted(d.keys())
    res = []
    for k in alphabetized_keys:
        res.append((k, d[k]))
    return res

def requestURL(baseurl, params = {}):
    req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
    prepped = req.prepare()
    return prepped.url

def get_with_caching(base_url, params_diction, cache_diction, cache_fname):
    full_url = requestURL(base_url, params_diction)
    # step 1
    if full_url in cache_diction:
        # step 2
        #print "retrieving cached result for " + full_url
        response_text = cache_diction[full_url]
    else:
        # step 3
        response = requests.get(base_url, params=params_diction)
        #print "adding cached result for " + full_url
        # add to the cache and save it permanently
        cache_diction[full_url] = response.text
        response_text = response.text
        fobj = open(cache_fname, "w")
        fobj.write(json.dumps(cache_diction))
        fobj.close()
    response_dictionary = json.loads(response_text)
    return response_dictionary

#----TMDB API-----
tmdb_cache_fname = "tmdb_cache_fname.txt"
try:
    tmdb_fobj = open(tmdb_cache_fname , 'r')
    tmdb_saved_cache = pickle.load(tmdb_fobj)
    tmdb_fobj.close()
except:
    tmdb_saved_cache = {}

    tmdb_url = 'http://api.themoviedb.org/3/movie/now_playing?api_key=a9318d1cc2a93a4f7bede01fde6d1f68'
    tmdb_params = {}
    tmdb_params['key'] = 'a9318d1cc2a93a4f7bede01fde6d1f68'
    result_dict = get_with_caching(tmdb_url, tmdb_params, cache_diction= tmdb_saved_cache, cache_fname=tmdb_cache_fname)

title = [each['title'] for each in result_dict['results']]
title.sort()
def movies_nearby(x):
    return "\n Here are the movies playing near you {}\n".format(x)

print movies_nearby(title)

class Movie():
    def __init__(self,post_dict={}):
        if 'Title' in post_dict:
            self.title = post_dict['Title']
        else:
            self.title = ""

        if 'Plot' in post_dict:
            self.plot = post_dict['Plot']
        else:
            self.plot = ""

        if 'imdbRating' in post_dict:
            self.rating = post_dict['imdbRating']
        else:
            self.rating = ""


        if 'Awards' in post_dict:
            self.awards = post_dict['Awards']
        else:
            self.awards = ""

        if 'imdbVotes' in post_dict:
            self.votes = post_dict['imdbVotes']
        else:
            self.votes = ""


    def __str__(self):
        #return "{}, is a movie a where {}. This film was given a {} rating by imdb. It has received {}.".format(self.title, self.plot, self.rating,  self.awards)
        if self.rating == "N/A":
            return "We have no data on the ratings.{}, is a movie a where {}. This film was given a {} rating by imdb and recived {} imdb votes. It has received {}.".format(self.title, self.plot, self.rating, self.votes, self.awards)
        elif float(self.rating) >=8:
            return "This movie is worth seeing! {}, is a movie a where {}. This film was given a {} rating by imdb and recived {} imdb votes. It has received {}.".format(self.title, self.plot, self.rating, self.votes, self.awards)
        elif float(self.rating) >=7:
            return "This movie got favorable reviews and is worth seeing! {}, is a movie a where {}. This film was given a {} rating by imdb and recived {} imdb votes. It has received {}.".format(self.title, self.plot, self.rating, self.votes, self.awards)
        elif float(self.rating)>=5:
            return "This movie is average! {}, is a movie a where {}. This film was given a {} rating by imdb and recived {} imdb votes. It has received {}.".format(self.title, self.plot, self.rating, self.votes, self.awards)
        elif float(self.rating)>=3:
            return "This movie has unfavorable reviews. Watch at your own risk. {}, is a movie a where {}. This film was given a {} rating by imdb and recived {} imdb votes. It has received {}.".format(self.title, self.plot, self.rating, self.votes, self.awards)
        elif float(self.rating)>=2:
             return "This movie was terrible do not watch it or watch at your own risk.{}, is a movie a where {}. This film was given a {} rating by imdb and recived {} imdb votes. It has received {}.".format(self.title, self.plot, self.rating, self.votes, self.awards)
#OMDB API
omdb_url = "http://www.omdbapi.com/?"
cache_fname = "omdb_cached_results.txt"

try:
    omdb_fobj = open(omdb_cache_fname, 'r')
    omdb_saved_cache = pickle.load(omdb_fobj)
    omdb_fobj.close()
    #print "retrieving cached result for OMDB"
except:
    omdb_saved_cache = {}
    #print "caching the result for OMDB"


    #title = ['Allied', 'Arrival', 'Fantastic Beasts and Where to Find Them', 'Genius', 'Hell or High Water', 'Inferno', 'Jack Reacher: Never Go Back', 'Mechanic: Resurrection', "Miss Peregrine's Home for Peculiar Children", 'Moana', 'Morgan', 'Nerve', 'Office Christmas Party', 'Rogue One: A Star Wars Story', 'Sausage Party', 'Snowden', 'Storks', 'Sully', 'The Infiltrator']
    for i in title:

        omdb_params = {'t':i, 'type' : "movie", 'r':'json'}
        omdb_dict = get_with_caching(omdb_url, omdb_params, cache_diction= omdb_saved_cache, cache_fname=cache_fname)
        x = Movie(omdb_dict)
    #x.score()
        print "-----------------------------------------------------------"
        print "Here is the Recommendation for the movie playing near you"
        print x

#---Mapquest API
quest_cache_fname = "quest_cached_results.txt"
try:
    quest_fobj = open(quest_cache_fname, 'r')
    quest_saved_cache = pickle.load(quest_fobj)
    quest_fobj.close()
    #print "retrieving cached result for Mapquest"
except:
    quest_saved_cache = {}
    #print "caching the result for Mapquest"

    quest_url = "http://www.mapquestapi.com/search/v2/radius"
    quest_params = {}
    quest_params['key'] = 'tQwNxNdstoKZqBqz9rSPBB1toeb4btv9'
    quest_params['origin'] = address
    quest_params['radius'] = 100
    quest_params['units'] = "m"
    quest_dict = get_with_caching(quest_url, quest_params, cache_diction= quest_saved_cache, cache_fname=quest_cache_fname)
man = quest_dict['searchResults']
name1 = [(name['name'], name['fields']['address'],name['fields']['city'], name['fields']['state'], name['fields']['postal_code'], name['fields']['phone']) for name in man]
#print name1
theater_location = []


def locations(x):

    for boy in x:

        if 'Cinema' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            return theater_location
        elif 'Cinemas' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            #print cinemaaddress
            return theater_location
        elif 'Theater' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            #print cinemaaddress
            return theater_location
        elif 'Theatre' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            #print cinemaaddress
            return theater_location
        elif 'Theatres' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            #print cinemaaddress
            return theater_location
        elif 'Movie' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            #print cinemaaddress
            return theater_location
        elif 'Movies' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            #print cinemaaddress
            return theater_location
        elif 'Theaters' in boy[0]:
            cinema_ddress =  (boy[1]).split(" ")
            city = boy[2].split(" ")
            city1 = j.join(city)
            cinemaaddress1 = j.join(cinema_ddress) , city1 , boy[3]
            cinemaaddress ='+'.join(cinemaaddress1)
            theater_location.append(cinemaaddress)
            #print cinemaaddress
            return theater_location
        else:
            theater_location.append(['4100+Carpenter+Rd+Ypsilanti+MI+48197'])
            #return theater_location
locations(name1)
#print locations(name1)

class Route():
    def __init__(self, x):
        self.distance = x['route']['distance']
        self.time = x['route']['time']
        self.hasHighway = x['route']['hasHighway']
    def time_mins(self):
        return float(self.time)/60
    def __str__(self):
        return "Your destination is {} miles away and it'll take you {} mins to arrive at your destination and the response to having highways is {}".format(self.distance, self.time_mins(), self.hasHighway)


mapquest_cache_fname = "mapquest_cached_results.txt"
try:
    mapquest_fobj = open(mapquest_cache_fname, 'r')
    mapquest_saved_cache = pickle.load(mapquest_fobj)
    mapquest_fobj.close()
    #print "retrieving cached result for OMDB"

except:
    mapquest_saved_cache = {}
    print "caching the result for OMDB"

    mapquest_url = 'http://www.mapquestapi.com/directions/v1/route?'
    mapquest_params = {}
    mapquest_params['key'] = 'tQwNxNdstoKZqBqz9rSPBB1toeb4btv9'
    mapquest_params['from'] = address
    mapquest_params['to'] = theater_location
    mapquest_dict = get_with_caching(mapquest_url, mapquest_params, cache_diction= mapquest_saved_cache, cache_fname= mapquest_cache_fname)
#print mapquest_dict
dest = Route(mapquest_dict)
print dest
maneuvers = mapquest_dict['route']['legs'][0]['maneuvers']
#print maneuvers
directions = [leg['narrative'] for leg in maneuvers]
#print directions
print "Here are the instructions to get to the closest theater to you that is actually playing the movies we suggested. "
for leg in maneuvers:
     instructions = leg['narrative']
     print instructions



class Tmdb(unittest.TestCase):
    def test_1(self):
        self.assertEqual(len(title), 20, "testing to see how many movies print out")
class Tmdb2(unittest.TestCase):
    def test_2(self):
        self.assertEqual(type(title), list)
class Directions(unittest.TestCase):
    def test_3(self):
        self.assertEqual(type(leg), dict)
        self.assertEqual(type(instructions), unicode)
class X(unittest.TestCase):
    def test_4(self):
        self.assertEqual(type(theater_location), list)
class dictionary(unittest.TestCase):
    def test_5(self):
        self.assertEqual(type(omdb_dict), dict)
class address(unittest.TestCase):
    def test_6(self):
        self.assertEqual(type(address), type)
class instruction(unittest.TestCase):
    def test_7(self):
        self.assertEqual(type(instructions[0]), unicode)
class mapquest(unittest.TestCase):
    def test_8(self):
        self.assertEqual(type(mapquest_dict), dict)

unittest.main(verbosity=2)
