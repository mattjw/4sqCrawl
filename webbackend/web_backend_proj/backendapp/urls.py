from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url( r'^/crawl/(\d+)/', include( 'backendapp.urls' ) )
    url( r'^/crawl/list/', include( 'backendapp.urls' ) )
    url( r'^/crawl/(\d+)/add_venue/', include( 'backendapp.urls' ) )
    url( r'^/crawl/(\d+)/remove_venue/', include( 'backendapp.urls' ) )
    url( r'^/crawl/(\d+)/delete/', include( 'backendapp.urls' ) )
    url( r'^/crawl/(\d+)/add_user', include( 'backendapp.urls' ) )
    url( r'^/crawl/(\d+)/remove_user', include( 'backendapp.urls' ) )
    url( r'^/user/(\d+)/', include( 'backendapp.urls' ) )
    url( r'^/user/create', include( 'backendapp.urls' ) )
    url( r'^/user/(\d+)/crawls', include( 'backendapp.urls' ) )
    url( r'^/checkin/', include( 'backendapp.urls' ) )

)