"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class MainTest(TestCase):
        
  def test( self ):
        client = Client()
        
        response = client.post( '/user/create/', {'foursq_id':"umanasd3"} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.post( '/user/create/', {'foursq_id':"umanasd3ddswe"} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.get( '/user/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.get( '/user/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        
        response = client.post( '/crawl/create/', { 'name' : 'a name',
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

        response = client.post( '/crawl/create/', { 'name' : 'another name',
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

        response = client.get( '/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/crawl/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/crawl/1/add_venue/', { 'venue_id' : 'somevenueid', 
                                                        'index' : '0' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/crawl/1/add_venue/', { 'venue_id' : 'someothervenueid', 
                                                        'index' : '0' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/crawl/1/remove_venue/', { 'venue_id' : 'someothervenueid' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/crawl/1/add_user/', { 'user_id' : 'umanasd3' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/crawl/1/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/crawl/1/remove_user/', { 'user_id' : 'umanasd3' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/crawl/1/', {}  )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/crawl/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.post( '/crawl/1/delete/', { 'user_id' : 'umanasd3' } )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40

        response = client.get( '/crawl/list/', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
