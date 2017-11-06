"""
this code handles rendering of initial login template and user verification.


superuser:
    username:vidursingh
    password:vidursingh

user:
    username:aditi
    password:revankar
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def login(request):
    return render(request, "login.html")       #render login template

def trying(request):
    data= request.POST      #getting post data
    username= data["username"]   #obtaining username
    password= data["password"]   #obtaining password
    user_authenticated = authenticate(username=username, password=password)     #inbuilt django function to try and authenticate user. user= None, if not authenticated
    if user_authenticated != None:   #if user is authenticated
        print("inside != none!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", request.user.username, request.user.get_username())
        return redirect('/orderfood')   #render the order-food page
    if user_authenticated !=None and (username == 'thehungercycle'): #Client Side login!
<<<<<<< HEAD
        return redirect ('/clientside/thc')
=======
        return redirect('/clientside/thc')
>>>>>>> 8b823baa4d10f151f0e0dc815e85f6ebb174f806

    else:  #if user is not authenticated
        return redirect('/login')   #go back to login page
