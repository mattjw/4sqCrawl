from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
  url( r'/callback$', 'frontendapp.views.callback' ),
  url( r'/auth$', 'frontendapp.views.auth' ),
  url( r'/done$', 'frontendapp.views.auth' ),  
)
