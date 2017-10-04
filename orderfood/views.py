from django.shortcuts import render
from django.http import HttpResponse
from orderfood.models import hungercycle, foodjunction

def inputorder(request):
    return render(request, "orderfood.html")


#this function stores the order.
def storeorder(request):
    inpt= request.POST  #getting post data as inpt
    outlet = inpt["outlet"]   #accessing parameters of data
    order = inpt["order"]
    username = request.user.username   #obtaining username of current user
    p = foodjunction(name=username, order=order)    #creating a record
    p.save()  #saving record
    for i in foodjunction.objects.all():   #debug statement, ignore.
        print(i)   #debug statement, ignore.
    return HttpResponse("order received")