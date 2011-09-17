# Create your views here.
import json
import datetime

from django.http import *
from django.shortcuts import render_to_response 
from django.core.exceptions import ObjectDoesNotExist

import models

def crawl_create( request ):

    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['name', 'description', 'startdatetime', 'duration', 'leader' ]
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
            
    name = params.get( 'name' )
    description = params.get( 'description' )
    startdatetime = params.get( 'startdatetime' )
    startdatetime = datetime.datetime.fromtimestamp(float(startdatetime))
    duration = params.get( 'duration' )
    leader_id = params.get( 'leader' )
    venues_ids = params.getlist( 'venues' )

    try:
        leader = models.User.objects.get( foursq_id=leader_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "User not found" )

    c = models.Crawl( name=name, description=description, startdatetime=startdatetime,
            duration=duration, leader=leader )

    for venue_id in venues_ids:
        v = Venue.objects.get_or_create( foursq_id=venue_id )
        v.save( )
        c.venues.append( v )
    
    c.save( )

    return HttpResponse('%d' % c.id)

def crawl_info( request, crawl_id ):

    try:
        c = models.Crawl.objects.get( id=crawl_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Crawl not found" )

    return HttpResponse( c.to_json( ) ) 

def crawl_list( request ):
    return HttpResponse( json.dumps( [ c.to_dict( ) for c in models.Crawl.objects.all( ) ] ) )

def crawl_add_venue( request, crawl_id ):

    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['venue_id', 'index']
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
            
    try:
        c = models.Crawl.objects.get( id=crawl_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Crawl not found" )    
    
    venue_foursq_id = params.get( 'venue_id' )
    v, created = models.Venue.objects.get_or_create( foursq_id=venue_foursq_id )
    v.save( )
    index = params.get( 'index' )

    voc_list = models.VenueOnCrawl.objects.filter( venue=v, crawl=c ).all()
    for voc in voc_list:
        if voc.index >= index:
            voc.index += 1
            voc.save( ) 

    voc, created = models.VenueOnCrawl.objects.get_or_create( venue=v, crawl=c, index=index )
    voc.save( )
    v.save( )
    c.save()
    return HttpResponse( 'ok' )

def crawl_remove_venue( request, crawl_id ):
    
    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['venue_id']
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
            
    try:
        c = models.Crawl.objects.get( id=crawl_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Crawl not found" )   

    venue_id = params.get( 'venue_id' )

    try:
        v = models.Venue.objects.get( foursq_id=venue_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Venue not found" )

    try:
        voc = models.VenueOnCrawl.objects.get( venue=v, crawl=c )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Venue Crawl combination not found" )        

    index = voc.index

    voc_list = models.VenueOnCrawl.objects.filter( venue=v, crawl=c ).all()
    for voc in voc_list:
        if voc.index > index:
            voc.index -= 1
            voc.save( )
    voc.delete()
    v.save()
    v.delete()
    return HttpResponse( 'ok' )

def crawl_delete( request, crawl_id ):

    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['user_id']
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
            
    try:
        c = models.Crawl.objects.get( id=crawl_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Crawl not found" ) 

    user_id = params.get( 'user_id' )

    try:
        u = models.User.objects.get( foursq_id=user_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "User not found" )         

    if c.leader.id == u.id:
        c.delete()
    
    return HttpResponse('ok')

def crawl_add_user( request, crawl_id ):

    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['user_id']
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
            
    try:
        c = models.Crawl.objects.get( id=crawl_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Crawl not found" ) 

    user_id = params.get( 'user_id' )

    try:
        u = models.User.objects.get( foursq_id=user_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "User not found" )  

    c.crawlers.add( u )
    u.save()
    c.save()

    return HttpResponse( 'ok' )


def crawl_remove_user( request, crawl_id ): 
    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['user_id']
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
            
    try:
        c = models.Crawl.objects.get( id=crawl_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Crawl not found" ) 

    user_id = params.get( 'user_id' )
    
    try:
        u = models.User.objects.get( foursq_id=user_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "User not found" )  
    c.crawlers.remove( u )
    u.save()
    c.save()

    return HttpResponse( 'ok' )




