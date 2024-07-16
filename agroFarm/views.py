from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from agroFarm.models import *

class Index(View):
    def get(self, request):
        return render(request,'index.html')
    
class Login_view(View):
    def get(self,request):
        alert_title = request.session.get('alert_title',False)
        alert_detail = request.session.get('alert_detail',False)
        if(alert_title):del(request.session['alert_title'])
        if(alert_detail):del(request.session['alert_detail'])
        context = {'alert_title':alert_title,
            'alert_detail':alert_detail,}
        return render(request,"login.html",context)
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:# checks if the user is logged in or not?
            login(request,user) #logins the user
            return redirect ('/')
        else:
            request.session['alert_title'] = "Invalid Login Attempt"
            request.session['alert_detail'] = "Please enter valid login credential."
            return redirect(request.path)
class Logout_view(View):
    def get(self,request):
        request.session.clear()
        logout(request)
        return redirect('/')
        