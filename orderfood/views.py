from django.shortcuts import render
from django.http import HttpResponse
from orderfood.models import hungercycle, foodjunction, foodjunction_menu


def chooseOutlet(request):
    return render(request, "chooseOutlet.html")


def inputorder(request):
    outletMap= {"foodjunction": foodjunction_menu,}
    outlet = request.get_full_path().split("/")[-2]
    out = outletMap[outlet].objects.all()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", type(out))
    for i in out:
        print(i)


    return render(request, "orderfood.html",{'out': out, "outlet":outlet})


#this function stores the order.
def storeorder(request):
    inpt= request.POST #getting post data as inpt
    print (inpt)
    #outlet = request.POST.get("outlet")   #accessing parameters of data
    outlet = inpt["outlet"]
    #order = request.POST.get('Order')
    order=""
    order_display_list=[]
    flag=False
    for i in request.POST:
        if inpt[i] and i not in ("csrfmiddlewaretoken", "outlet"):
            item= i.split("-")[0]
            order_display_list+= [item+ str(inpt[i])+","]
            order= order + str(inpt[i]) + "-" + str(item) + ","
    username = request.user.get_username()   #obtaining username of current user
    if(outlet=="foodjunction"):
        p = foodjunction(name=username, order=order, status= "open")    #creating a record
        p.save()  #saving record
    if(outlet=="hunger cycle"):
        p = hungercycle(name=username, order = order, status = "open" )
        p.save()
    return render(request, "orderaccepted.html", {'p': p})