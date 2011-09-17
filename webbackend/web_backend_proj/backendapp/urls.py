from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url( r'^crawl/create/', 'backendapp.views.crawl_create' ),
    # POST request
    #
    # params:
    # name              name for the crawl
    # description       description of the crawl
    # startdatetime     start date of the time as seconds after epoch
    # duration          duration of the crawl in minutes
    # leader            user_id of the crawl leader
    # venues            list of foursq_ids of venues on the crawl
    #
    # adds a crawl to the system. Returns the crawl_id
    url( r'^crawl/(\d+)/', include( 'backendapp.urls' ) ),
    # GET request
    #
    # returns info for the crawl
    url( r'^crawl/list/$', include( 'backendapp.urls' ) ),
    # GET request
    #
    # returns all crawls in the system
    url( r'^crawl/(\d+)/add_venue/$', include( 'backendapp.urls' ) ),
    # POST request.
    #
    # params:
    # venue_id      foursq_id of the venue to add to the crawl
    # index         the index of the venue within the crawl
    #
    # inserts a venue to the crawl at the specified index
    url( r'^crawl/(\d+)/remove_venue/$', include( 'backendapp.urls' ) ),
    # POST request.
    #
    # params:
    # venue_id      the index of the venue to remove from the crawl
    #
    # removes the venue from the crawl
    url( r'^crawl/(\d+)/delete/$', include( 'backendapp.urls' ) ),
    # POST request.
    #
    # params:
    # user_id       the ID of the requesting user
    #
    # deletes the crawl
    url( r'^crawl/(\d+)/add_user/$', include( 'backendapp.urls' ) ),
    # POST request.
    #
    # params:
    # user_id       the user to add to the crawl
    url( r'^crawl/(\d+)/remove_user/$', include( 'backendapp.urls' ) ),
    # POST request
    #
    # params:
    # user_id       the user to remove from the crawl
    url( r'^user/(\d+)/$', 'backendapp.views.user_id' ),
    # GET request
    #
    # returns info for the user
    url( r'^user/create$', 'backendapp.views.user_create' ),
    # POST request
    #
    # params:
    # foursq_id     the foursq_id of the user
    #
    # create a user
    url( r'^user/(\d+)/crawls$', 'backendapp.views.user_id_crawls' ),
    url( r'^user/list$', 'backendapp.views.user_list' ),
    # GET request
    #
    # returns the list of crawls the user has been on
    url( r'^checkin/$', include( 'backendapp.urls' ) )
    # POST request
    #
    # params:
    # venue_id
    # crawl_id
    # user_id
    # 
    # performs a checkin on the service. 
)