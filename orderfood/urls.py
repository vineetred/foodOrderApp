from django.conf.urls import url
from .views import inputorder, storeorder

urlpatterns = [
    url(r'^/$', inputorder),
    url(r'^/orderaccepted$', storeorder),
]




