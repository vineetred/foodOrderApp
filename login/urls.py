#this part of the code tells django what to do depending on the url. It calls functions from the .views file for each url.


from django.conf.urls import url
from .views import login,trying  #importing functions from the .views file

urlpatterns = [
    url(r'^/$', login),   #calling "login" function
    url(r'trying$', trying),    #calling "trying" function
]





