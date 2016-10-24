from django.conf.urls import url, include
from django.contrib import admin
from main import urls as mainURLS
from marvel import urls as marvelURLS


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^marvel/',
    	include(marvelURLS)),
    url(r'^',
    	include(mainURLS)),
]
