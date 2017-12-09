from django.shortcuts import render
from orderfood.models import foodjunction, hungercycle
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from orderfood.models import hungercycle, foodjunction


def orderHistory(request):
    username= request.user.username
    orderList= foodjunction.objects.all().filter(name= username)
    for i in orderList:
        print(i)
    return render(request, "orderHistory.html", {'orderList': orderList})