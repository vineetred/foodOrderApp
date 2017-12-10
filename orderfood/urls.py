from django.conf.urls import url
from .views import inputorder, storeorder, chooseOutlet,success

urlpatterns = [
    url(r'^/$', chooseOutlet),
    url(r'^/orderaccepted$', storeorder),
    url(r'^/yes$',success),
    url(r'^/[a-zA-Z.]', inputorder),

]




