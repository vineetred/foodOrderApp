#this is the base of all url mapping. Code comes here FIRST to check for url patterns


from django.conf.urls import url
from django.contrib import admin
from login import urls as loginurls
from django.conf.urls import include
from login.views import login
import login.urls as loginurls
import orderfood.urls as orderfoodurls
import clientSide.urls as clientSideurls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', include(loginurls)),
    url(r'^orderfood', include(orderfoodurls)),
    url(r'^client', include(clientSideurls)),

    
]
