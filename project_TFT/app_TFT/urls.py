from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = patterns('',
    # home page     
    url(r'^$', 'app_TFT.views.home',name='home'),
    # tool page 
    url(r'^$', 'app_TFT.views.app',name='app'), 
    
    # course page 
    url(r'^course/(?P<id>\d+)$', 'app_TFT.views.course', name='course'),


    # login/logout
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'page_login.html'},name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login',name="logout"),

    # upload
    url(r'^upload$', 'app_TFT.views_upload.upload',name='upload'),
    
)


