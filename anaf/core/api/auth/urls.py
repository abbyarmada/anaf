from django.conf.urls import patterns, url


urlpatterns = patterns('anaf.core.api.auth.views',
                       url(r'^get_request_token$', 'get_request_token',
                           name="api_get_request_token"),
                       url(r'^authorize_request_token$', 'authorize_request_token',
                           name="api_authorize_request_token"),
                       url(r'^get_access_token$', 'get_access_token',
                           name="api_get_access_token"),
                       )
