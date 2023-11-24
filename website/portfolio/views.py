from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request,"portfolio/home.html")
def about(request):
    return render(request,"portfolio/about.html")
def contact(request):
    return render(request,"portfolio/contact.html")