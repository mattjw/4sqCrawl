"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

checkin_json = """
{
    "id": "4checkinid4e0c00032eeac3",
    "createdAt": 1300001600,
    "type": "checkin",
    "timeZone": "America/New_York",
    "user": {
        "id": "66userid10",
        "firstName": "Jimmy",
        "lastName": "Foursquare",
        "photo": "https://foursquare.com/img/blank_boy.png",
        "gender": "male",
        "homeCity": "New York, NY",
        "relationship": "self"
    },
    "venue": {
        "id": "99venueid10",
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

class MainTest(TestCase):
        
  def test( self ):
        client = Client()
        
        response = client.post( '/api/user/create/', {'foursq_id':"umanasd3"} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.post( '/api/user/create/', {'foursq_id':"umanasd3ddswe"} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.get( '/api/user/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.get( '/api/user/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.post( '/api/crawl/create/', { 'name' : 'a name',
                        'description' : 'a description',
                        'startdatetime' : '1316277933',
                        'duration' : '30', 
                        'leader' : 'umanasd3',
                        'venues' : [] } ) 
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/create/', { 'name' : 'another name',
                        'description' : 'another description',
                        'startdatetime' : '1316277933',
                        'duration' : '30', 
                        'leader' : 'umanasd3ddswe',
                        'venues' : [] } ) 
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/1/add_venue/', { 'venue_id' : 'somevenueid', 
                                                        'index' : '0' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/1/add_venue/', { 'venue_id' : 'someothervenueid', 
                                                        'index' : '0' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/1/remove_venue/', { 'venue_id' : 'someothervenueid' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/1/add_user/', { 'user_id' : 'umanasd3' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/2/add_user/', { 'user_id' : 'umanasd3' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40



        print 'USER CRAWLS'
        response = client.get( '/api/user/1/crawls/', {} ) 
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/1/remove_user/', { 'user_id' : 'umanasd3' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/1/', {}  )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/user/1/crawls/', {} ) 
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/api/crawl/1/delete/', { 'user_id' : 'umanasd3' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/api/crawl/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        
        
        
        print " \n\n\n BIG CRAWL TEST \n\n\n"

        print " "*10 + "USERS"

        response = client.post( '/api/user/create/', {'foursq_id':"66useridleader09"} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.post( '/api/user/create/', {'foursq_id':"66userid10"} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.post( '/api/user/create/', {'foursq_id':"66userid11"} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        
        
        print " "*10 + "CRAWL (+USERS)"
        
        response = client.post( '/api/crawl/create/', { 'name' : 'Crawl Name',
                        'description' : 'Crawl description',
                        'startdatetime' : '1300000000',  #secs from epoch
                        'duration' : '30', # minutes   # finish time becomes 1300001800
                        'leader' : '66useridleader09',
                        'venues' : ['99venueid10','99venueid11'] } ) 
                        # id should be crawl 3
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.get( '/api/crawl/3/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.post( '/api/crawl/3/add_user/', { 'user_id' : '66userid10' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        
        print " "*10 + "PUSH RECEIVER"
        
        response = client.post( '/receiver/', { 'checkin' : checkin_json } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        # manual checkin:
        # venue: 99venueid10
        # user: 66userid10
        # time: ...








