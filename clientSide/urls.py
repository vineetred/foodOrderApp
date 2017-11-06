from django.conf.urls import url
from .views import clientLogin

urlpatterns = [
    url(r'^/$', clientLogin),   #calling "Clientlogin" function
]
