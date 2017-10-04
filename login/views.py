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
    user = authenticate(username=username, password=password)     #inbuilt django function to try and authenticate user. user= None, if not authenticated
    if user != None:   #if user is authenticated
        return redirect('/orderfood')   #render the order-food page
    else:  #if user is not authenticated
        return redirect('/login')   #go back to login page