from django.conf.urls import url
from .views import inputorder, storeorder, chooseOutlet

urlpatterns = [
    url(r'^/$', chooseOutlet),
    url(r'^orderfood/', ),
    url(r'^/orderaccepted$', storeorder),
]




