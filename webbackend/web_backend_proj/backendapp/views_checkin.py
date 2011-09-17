from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist

from django import forms
import models 

from datetime import datetime 

# Create your views here.

def checkin_create( request ):
    """
    r'^/checkin/create' 
    # venue_id
    # crawl_id
    # user_id
    """
    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['venue_id','crawl_id','user_id']
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
    
    #
    # Process
    venue_id = params['venue_id']
    crawl_id = params['crawl_id']
    user_id = params['user_id']

    try:
        venue_obj = models.Venue.objects.get( id=venue_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Venue ID not found" )

    try:
        crawl_obj = models.Crawl.objects.get( id=crawl_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "Crawl ID not found" )
    
    try:
        user_obj = models.User.objects.get( id=user_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "User ID not found" )
        
    vis_obj = Visited( venue=venue_obj, crawl=crawl_obj, user=user_obj)
    vis_obj.save()
    
    return HttpResponse("checkin create" )
    
    
    
    
    
    
    
    
    
    
    
