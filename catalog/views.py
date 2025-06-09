from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "catalogs/home.html")
    return HttpResponse("YES")

def contacts(request):
    if request.method == "GET":
        return render(request, "catalogs/contacts.html")
    return HttpResponse("YES")
