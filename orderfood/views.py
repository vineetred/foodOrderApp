from django.shortcuts import render
from django.http import HttpResponse
from orderfood.models import hungercycle, foodjunction, foodjunction_menu

def inputorder(request):
<<<<<<< HEAD
    q = foodjunction.objects.values_list('order').filter(status="open").order_by('status')
    out = foodjunction_menu.objects.values_list('foodItem','foodPrice')
=======
    out = foodjunction.objects.all()
>>>>>>> 011996adc511c42b3511e7dd8b984a795bee6221
    return render(request, "orderfood.html",{'out': out})


#this function stores the order.
def storeorder(request):
    #inpt= request.POST #getting post data as inpt
    outlet = request.POST.get('outlet')   #accessing parameters of data
    #order = inpt["Order"]
    order = request.POST.get('Order')
    username = request.user.get_username()   #obtaining username of current user
    print(username, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if(outlet=="foodjunction"):
        p = foodjunction(name=username, order=order, status= "open")    #creating a record
        p.save()  #saving record
    if(outlet=="hunger cycle"):
        p = hungercycle(name=username, order = order, status = "open" )
        p.save()

    return render(request, "orderaccepted.html",{'p': p})