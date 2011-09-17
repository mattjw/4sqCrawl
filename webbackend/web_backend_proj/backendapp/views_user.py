from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Template, Context, RequestContext
from django.template.loader import get_template

from django import forms
import models 

from datetime import datetime 

# Create your views here.

def user_id( request, user_id ):
    """
    r'^/user/(\d+)/'
    """
    
    return HttpResponse("user_id"+args)

def user_list( request ):
    """
    r'^/user/list/'
    """
    user_objs = models.Users.objects.all()
    str = ''.join( [obj.foursq_id for obj in user_objs] )
    return 

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
            return HttpResponseBadRequest( "Missing require field: " + req_param )
    
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
    return HttpResponse("user_id_crawls" )





