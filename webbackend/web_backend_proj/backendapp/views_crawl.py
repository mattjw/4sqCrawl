# Create your views here.
import json

from django.http import *
from django.shortcuts import render_to_response 

from models import *

def crawl_create( request ):

    name = request.POST.get( 'name' )
    description = request.POST.get( 'description' )
    startdatetime = request.POST.get( 'startdatetime' )
    duration = request.POST.get( 'duration' )
    leader_id = request.POST.get( 'leader' )
    venues_ids = request.POST.getlist( 'venues' )

    leader = User.objects.get_or_create( foursq_id=leader_id )

    c = Crawl( name=name, description=description, startdatetime=startdatetime,
            duration=duration, leader=leader)
    for venue_id in venues_ids:
        v = Venue.objects.get_or_create( foursq_id=venue_id )
        c.venues.append( v )
    c.save()


def crawl_info( request, crawl_id ):
    c = Crawl.objects.get( id=crawl_id )
    return HttpResponse( c.to_json( ) ) 

def crawl_list( request ):
    return HttpResponse( json.dumps( [ c.to_json( ) for c in Crawl.objects.all( ) ] ) )

def crawl_add_venue( request, crawl_id ):
    c = Crawl.objects.get( id=crawl_id )
    
    venue_foursq_id = request.POST.get( 'foursq_id' )
    v = Venue.objects.get_or_create( foursq_id=venue_foursq_id )

    index = request.POST.get( 'index' )

    voc_list = VenueOnCrawl.objects.filter( venue=v, crawl=c )
    for voc in voc_list:
        if voc.index >= index:
            voc.index += 1
            voc.save( ) 

    voc = VenueOnCrawl.objects.get_or_create( venue=v, crawl=c, index=i )

def crawl_remove_venue( request, crawl_id ):

def crawl_delete( request, crawl_id ):

def crawl_add_user( request, crawl_id ):

def crawl_remove_user( request, crawl_id ): 