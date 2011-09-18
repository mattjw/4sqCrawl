from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
  url( r'callback/?$', 'frontendapp.views.callback', name='oauth_callback' ),
  url( r'auth/?$', 'frontendapp.views.auth', name='oauth_auth' ),
  url( r'done/?$', 'frontendapp.views.done', name='oauth_done' ),
  url( r'front/?$', 'frontendapp.views.front', name='oauth_front' ),
  url( r'receiver/?$', 'frontendapp.views.push_receiver', name='push_receiver' ),
)
