# from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context={
        'users':User.objects.all()
    }
    return render(request, "index.html", context)

def createUser(request):
    User.objects.create(first_name=request.POST['first_name'],
    last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])
    return redirect('/')
