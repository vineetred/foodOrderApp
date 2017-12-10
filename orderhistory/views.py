from django.shortcuts import render
from orderfood.models import foodjunction, hungercycle
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from orderfood.models import hungercycle, foodjunction


def orderHistory(request):
    username= request.user.username
    orderListFoodjunction_open= foodjunction.objects.all().filter(name= username).filter(status= "open")
    orderListFoodjunction_close= foodjunction.objects.all().filter(name= username).filter(status= "close")
    orderListHungercycle_open = hungercycle.objects.all().filter(name=username).filter(status= "open")
    orderListHungercycle_close = hungercycle.objects.all().filter(name=username).filter(status= "close")

    #for i in range(len(orderList)):
    #    orderList[i]= str(orderList[i]).strip(username)
    return render(request, "orderHistory.html", {'orderListFoodjunction_open': orderListFoodjunction_open,
                                                 'orderListFoodjunction_close': orderListFoodjunction_close,
                                                 'orderListHungercycle_close': orderListHungercycle_close,
                                                 'orderListHungercycle_open': orderListHungercycle_open})