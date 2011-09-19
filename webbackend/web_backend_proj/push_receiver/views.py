import urllib
import urllib2
import json
import datetime 

from django.http import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

from django.core.exceptions import ObjectDoesNotExist

import os
import os.path

import backendapp.models

# Create your views here.

import credentials 

def push_receiver( request ):
    if request.method == 'POST':
        params = request.POST
        
        if "checkin" in params:
            checkin_jsonstr = params['checkin']
            checkin = json.loads( checkin_jsonstr )
            
            foursq_venue_id = checkin['venue']['id']
            foursq_user_id = checkin['user']['id']
            created_at_unix = float( checkin['createdAt'] )
            created_at = datetime.datetime.fromtimestamp(float(created_at_unix))
            
            #
            # register the checkin in the DBase
            
            # Need to:
            #    check venue is in DB. check user is in DB.
            #    find a matching crawl: a crawl for the given venue id and user id
            #    finally, check that the checkin is after crawl
            
            try:
                user_obj = backendapp.models.User.objects.get( foursq_id=foursq_user_id )
            except ObjectDoesNotExist:
                return HttpResponse( "unkown foursq user id" )
                
            try:
                venue_obj = backendapp.models.Venue.objects.get( foursq_id=foursq_venue_id )
            except ObjectDoesNotExist:
                return HttpResponse( "unkown foursq user id" )
            
            
            crawls_haystack = backendapp.models.Crawl.objects
            crawls_haystack = crawls_haystack.filter( startdatetime__lte=created_at )
                # only keep those crawls with start time less than or equal to
                # checkin time
            
            created_at_offset = created_at  # - datetime.timedelta(hours=12)
            crawls_haystack = crawls_haystack.filter( enddatetime__gte=created_at_offset )
            
            # crawls_haystack is a list of crawls where the pushed checkin's
            # timestamp is within the crawl's start and end time.
            #
            # we should now narrow down the haystack to find a crawl
            # matching the checkin's user and venue
            
            candidate_crawls = []
            
            for crawl in crawls_haystack:
                crawls_venues = crawl.venues.all()  # all venues on this crawl
                crawls_venues_ids = [ v.foursq_id for v in crawls_venues ]
                
                crawls_users = crawl.crawlers.all()  # all users on this crawl
                crawls_users_ids = [ v.foursq_id for v in crawls_users ]
                
                if ( (foursq_venue_id in crawls_venues_ids) and
                    ( foursq_user_id in crawls_users_ids ) ):
                    candidate_crawls.append( crawl )
            
            #
            # at this point, candidate_crawls is a list of crawls where...
            #     the time of this checkin is during the crawl's time limit
            #     the checkin's user is on the crawl
            #     the checkin's venue is part of the crawl
            # There may be multiple crawls (if the user signs up for
            # multiple crawls at the same time covering overlapping venues.

            if len( candidate_crawls ) >= 1:
                # do something dumb -- use the first valid crawl
                valid_crawl = candidate_crawls[0]
                
                visit_obj, was_created = backendapp.models.Visited.objects.get_or_create( venue=venue_obj, user=user_obj, crawl=valid_crawl )
                return HttpResponse( "visit recorded: " + str(visit_obj) + "        was created: " + str(was_created) )
            
            return HttpResponse("checkin not on any matching crawl. no change made.")
            
            return HttpResponse( "candidates: " + str(candidate_crawls) )
            return HttpResponse( str(crawls_venues_ids) + " " + str(crawls_users_ids) )
            return HttpResponse( str(crawls_haystack) )

        return HttpResponse( "No checkins param" )
 
    return HttpResponse("No POST")


