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
        
        response = client.post( '/user/create', {'foursq_id':3} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
        
        response = client.get( '/user/list', {} )
        print "#"*40
        print response.content
        print "#"*40
        print response.status_code
        print "#"*40
