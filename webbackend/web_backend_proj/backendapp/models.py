from django.db import models

# Create your models here.


class User( models.Model ):
    foursq_id = models.CharField( max_length=100 )

class Venue( models.Model ):
    foursq_id = models.CharField( max_length=100 )

class Crawl( models.Model ):
    start_loc = models.ForeignKey( Venue, 
                    related_name="start_of" )
    end_loc = models.ForeignKey( Venue,
                    related_name="end_of" )
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

class VenueOnCrawl( models.Model ):
    index = models.IntegerField()
    venue = models.ForeignKey( Venue )
    crawl = models.ForeignKey( Crawl )
    
class Visited( models.Model ):
    venue = models.ForeignKey( Venue, related_name="visited" )
    crawl = models.ForeignKey( Crawl, related_name="visited" )
    user = models.ForeignKey( User, related_name="visited" )

























