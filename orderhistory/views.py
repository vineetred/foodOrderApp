from django.shortcuts import render
from orderfood.models import foodjunction, hungercycle
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from orderfood.models import hungercycle, foodjunction


def orderHistory(request):
    username= request.user.username
    orderListFoodjunction= foodjunction.objects.all().filter(name= username)
    orderListHungercycle = hungercycle.objects.all().filter(name=username)
    #for i in range(len(orderList)):
    #    orderList[i]= str(orderList[i]).strip(username)
    return render(request, "orderHistory.html", {'orderListFoodjunction': orderListFoodjunction,'orderListHungercycle': orderListHungercycle})