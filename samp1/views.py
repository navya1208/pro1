from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<img src="https://cdn.pixabay.com/photo/2020/07/09/17/39/puppy-5388151__340.jpg"><h1>Welcome to MYWEBSITE</h1>')#HttpResponse(HTML tag as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to homepage<h1>")

def html_dem1(request):
    return render(request,"dem1.html")

def html_dem2(request):
    return render(request,"dem2.html")