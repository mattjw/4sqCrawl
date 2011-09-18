from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from django import forms
import models 
import json

from datetime import datetime 

# Create your views here.

def user_id( request, user_id ):
    """
    r'^/user/(\d+)/'
    """
    try:
        obj = models.User.objects.get( id=user_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "User not found" )
    json_str = obj.to_json()
    return HttpResponse( json_str )

def user_list( request ):
    """
    r'^/user/list/'
    """
    return HttpResponse( json.dumps( [ u.to_dict( ) for u in models.User.objects.all( ) ] ) )

def user_create( request ):
    """
    r'^/user/create' 
    """
    #
    # Extract and validate
    if request.method != 'POST':
        return HttpResponseBadRequest( "POST calls only" )
    
    params = request.POST
    
    req_params = ['foursq_id',]
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing required field: " + req_param )
    
    #
    # Process
    foursq_id = params['foursq_id']
    
    usr = models.User(foursq_id=foursq_id)
    usr.save()
    
    return HttpResponse("user_create" )

def user_id_crawls( request, user_id ):
    """
    r'^/user/(\d+)/crawls'
    """
    try:
        obj = models.User.objects.get( id=user_id )
    except ObjectDoesNotExist:
        return HttpResponseBadRequest( "User not found" )
    return HttpResponse( json.dumps( [ c.to_dict( ) for c in obj.on_crawls.all( ) ] ) )





