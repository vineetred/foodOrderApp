from django.conf.urls import url
from .views import inputorder, storeorder, chooseOutlet

urlpatterns = [
    url(r'^/$', chooseOutlet),
    url(r'^/orderaccepted$', storeorder),
    url(r'^/[a-zA-Z.]', inputorder),

]




