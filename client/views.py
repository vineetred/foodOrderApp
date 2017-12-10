from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from orderfood.models import hungercycle, foodjunction

# Create your views here.
def clientLogin(request):
    return render(request, "client/home.html")

def clientAuth(request):
    data= request.POST      #getting post data
    username= data["username"]   #obtaining username
    password= data["password"]   #obtaining password
    user_authenticated = authenticate(username=username, password=password)     #inbuilt django function to try and authenticate user. user= None, if not authenticated
    if user_authenticated != None:   #if user is authenticated
        print("inside != none!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", request.user.username, request.user.get_username())
        return redirect('/client/order')   #render the order-food page

    else:  #if user is not authenticated
        return redirect('/client')   #go back to login page

def order(request):
    print ("2222222222222222222222222222222222222222", request.user.username)
    if request.user.username== "foodjunction":
        orderList= foodjunction.objects.all().filter(status="open")
    elif request.user.username== "hungercycle":
        orderList = hungercycle.objects.all().filter(status="open")
    else:
        orderList =  foodjunction.objects.all().filter(status="open")
    for order in orderList:
        print(order.id)
    return render(request, "client/order.html",{'orderList':orderList})

def done(request):
    #data = request.POST.get("Order")
    mark = request.POST.get("Order")
    print (">>>>>>>>>>>>>>>>>>>", mark)
    obj= foodjunction.objects.get(pk = mark)
    print(">>>>>>>>>>>>>>>>>>>>>>>",obj.status)
    obj.status="close"
    obj.save()
    
    return redirect('/client/order')


 