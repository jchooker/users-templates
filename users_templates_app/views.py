from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {

    }

    return render(request, "index.html", context)
    # return HttpResponse("this")
