from django.db import models
import json
import time
import datetime
# Create your models here.


class User( models.Model ):
    foursq_id = models.CharField( max_length=100 )

    def to_json( self ):
        return json.dumps( self.to_dict( ) )

    def to_dict( self ):
        return { 'user' : { 'id': self.id, 'foursq_id' : self.foursq_id } }
    

class Venue( models.Model ):
    foursq_id = models.CharField( max_length=100 )

    def to_json( self ):
        return json.dumps( self.to_dict( ) ) 
    
    def to_dict( self ):
        return { 'venue' : { 'id' : self.id, 'foursq_id' : self.foursq_id } }

class Crawl( models.Model ):
    duration = models.IntegerField()
    name = models.CharField( max_length=100 )
    description = models.CharField( max_length=1000 )
    startdatetime = models.DateTimeField( 'start datetime' )
    
    leader = models.ForeignKey( User, verbose_name="The leader of this crawl.",
                related_name="led_by" )
    crawlers = models.ManyToManyField( User, through=None, 
                verbose_name="The crawlers participating in the crawl.",
                related_name="on_crawls" )
    venues = models.ManyToManyField( Venue, through='VenueOnCrawl',
                verbose_name="The venues that are part of the route on the crawl.",
                related_name="on_crawls")

    def to_json( self ):
        return json.dumps( self.to_dict( ) )
    
    def to_dict( self ):
        return { 'crawl' : { 'id' : self.id, 'name' : self.name, 'description' : self.description,
                'startdatetime' : time.mktime( self.startdatetime.timetuple( ) ),
                'leader' : self.leader.to_dict( ), 'duration' : self.duration, 
                'crawlers' : [ u.to_dict( ) for u in self.crawlers.all() ],
                'venues' : [ v.to_dict( ) for v in self.venues.all() ]
        } }

class VenueOnCrawl( models.Model ):
    index = models.IntegerField()
    venue = models.ForeignKey( Venue )
    crawl = models.ForeignKey( Crawl )

class Visited( models.Model ):
    venue = models.ForeignKey( Venue, related_name="visited" )
    crawl = models.ForeignKey( Crawl, related_name="visited" )
    user = models.ForeignKey( User, related_name="visited" )
    #visit_time = models.DateTimeField( 'visit_time' ) #~
























