from django.shortcuts import render
from django.http import HttpResponse
from orderfood.models import hungercycle, foodjunction

def inputorder(request):
    out = foodjunction.objects.all()
    return render(request, "orderfood.html",{'out': out})


#this function stores the order.
def storeorder(request):
    inpt= request.POST  #getting post data as inpt
    outlet = inpt["outlet"]   #accessing parameters of data
    order = inpt["order"]
    username = request.user.get_username()   #obtaining username of current user
    print(username, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if(outlet=="foodjunction"):
        p = foodjunction(name=username, order=order, status= "open")    #creating a record
        p.save()  #saving record
    if(outlet=="hunger cycle"):
        p = hungercycle(name=username, order = order, status = "open" )
        p.save()

    return render(request, "orderaccepted.html",{'p': p})