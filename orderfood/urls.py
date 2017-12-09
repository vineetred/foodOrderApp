from django.conf.urls import url
from .views import inputorder, storeorder, chooseOutlet

urlpatterns = [
    url(r'^/$', chooseOutlet),
    url(r'^/foodjunction/$', inputorder),
    url(r'^/orderaccepted$', storeorder),
]




