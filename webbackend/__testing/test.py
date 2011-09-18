import urllib2
import urllib

checkin_jsonstr = """
{
    "id": "4e6fe1404b90c00032eeac34",
    "createdAt": 1315955008,
    "type": "checkin",
    "timeZone": "America/New_York",
    "user": {
        "id": "1",
        "firstName": "Jimmy",
        "lastName": "Foursquare",
        "photo": "https://foursquare.com/img/blank_boy.png",
        "gender": "male",
        "homeCity": "New York, NY",
        "relationship": "self"
    },
    "venue": {
        "id": "4ab7e57cf964a5205f7b20e3",
        "name": "foursquare HQ",
        "contact": {
            "twitter": "foursquare"
        },
        "location": {
            "address": "East Village",
            "lat": 40.72809214560253,
            "lng": -73.99112284183502,
            "city": "New York",
            "state": "NY",
            "postalCode": "10003",
            "country": "USA"
        },
        "categories": [
            {
                "id": "4bf58dd8d48988d125941735",
                "name": "Tech Startup",
                "pluralName": "Tech Startups",
                "shortName": "Tech Startup",
                "icon": "https://foursquare.com/img/categories/building/default.png",
                "parents": [
                    "Professional & Other Places",
                    "Offices"
                ],
                "primary": true
            }
        ],
        "verified": true,
        "stats": {
            "checkinsCount": 7313,
            "usersCount": 565,
            "tipCount": 128
        },
        "url": "http://foursquare.com"
    }
}
"""





"""
## TEST 1 ##
values = {}
values['foursq_id'] = 'some_user_id'

data = urllib.urlencode(values)

url = 'https://fourcrawl.nomovingparts.net/api/user/create/'

req = urllib2.Request(url, data=data) 
response = urllib2.urlopen( req ) 
reply = response.read()
print reply
"""


"""
## TEST 2 ##
values = {}
values['foursq_id'] = 'some_user_id'

data = urllib.urlencode(values)

url = 'https://fourcrawl.nomovingparts.net/receiver/'

req = urllib2.Request(url, data=data) 
response = urllib2.urlopen( req ) 
reply = response.read()
print reply
"""


## TEST 3 ##
"""
values = {}
values['foursq_id'] = 'some_user_id'

data = urllib.urlencode(values)

url = 'https://fourcrawl.nomovingparts.net/api/user/1/'

req = urllib2.Request(url, data=data) 
response = urllib2.urlopen( req ) 
reply = response.read()
print reply
"""






## TEST 4 ##
values = {}
values['checkin'] = checkin_jsonstr

data = urllib.urlencode(values)

url = 'https://fourcrawl.nomovingparts.net/receiver/'

req = urllib2.Request(url, data=data) 
response = urllib2.urlopen( req ) 
reply = response.read()
print reply



exit()










                        
                        
## TEST 5 ##
values = { 'name' : 'Crawl Name',
                        'description' : 'Crawl description',
                        'startdatetime' : '1300000000',  #secs from epoch
                        'duration' : '30', # minutes   # finish time becomes 1300001800
                        'leader' : '790204',
                        'venues' : ['99venueid10','99venueid11'] } 

data = urllib.urlencode(values)

url = 'https://fourcrawl.nomovingparts.net/api/crawl/create/'

req = urllib2.Request(url, data=data) 
response = urllib2.urlopen( req ) 
reply = response.read()
print reply