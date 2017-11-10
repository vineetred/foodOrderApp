from django.conf.urls import url
from .views import clientLogin, clientAuth, order,done

urlpatterns = [
    url(r'^/$', clientLogin),
    url(r'^/edit', clientAuth),
    url(r'^/order', order),
    url(r'^/done', done),
    
]




