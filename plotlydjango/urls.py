from django.conf.urls import url, include
from django.contrib import admin
from  home.views import home
from plotlydjango.settings import *











urlpatterns = [
    url(r'', include('home.urls')),
     url(r'^admin/', admin.site.urls),
]
 


