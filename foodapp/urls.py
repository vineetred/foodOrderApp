#this is the base of all url mapping. Code comes here FIRST to check for url patterns


from django.conf.urls import url
from django.contrib import admin
from login import urls as loginurls
from django.conf.urls import include
from login.views import login
import login.urls as loginurls
import orderfood.urls as orderfoodurls
import client.urls as clientSideurls
import orderhistory.urls as orderHistoryUrls
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', include(loginurls)),
    url(r'^orderfood', include(orderfoodurls)),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^client', include (clientSideurls)),
    url(r'^accounts', include('accounts.urls')),
    url(r'^orderhistory', include(orderHistoryUrls)),


    

    
]
