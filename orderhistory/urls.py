from django.conf.urls import url
from .views import orderHistory

urlpatterns = [
    url(r'^/$', orderHistory),
]



