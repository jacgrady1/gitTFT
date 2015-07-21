from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings

# ... your normal urlpatterns here



urlpatterns = patterns('',
    # home page     
    url(r'^$', 'app_TFT.views.home',name='home'),

    # course page /(?P<id>\d+) 
    url(r'^course/(?P<id>\d+)$', 'app_TFT.views.course', name='course'),

    # login/logout
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'page_login.html'},name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login',name="logout"),

    
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))