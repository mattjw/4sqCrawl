from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_backend_proj.views.home', name='home'),
    # url(r'^web_backend_proj/', include('web_backend_proj.foo.urls')),
    url( r'^api', include( 'backendapp.urls' ) ),
    url( r'^receiver/?$', 'push_receiver.views.push_receiver' ),
    url( r'^/?$', direct_to_template, {'template':'home.html'} ),
    url( r'^createcrawl/?$', direct_to_template, {'template':'createcrawl.html'} ),
    url( r'^viewcrawl/?$', direct_to_template, {'template':'viewcrawl.html'} ),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
