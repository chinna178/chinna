from django.http import HttpResponse
from django.shortcuts import render
import requests

def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse('about')
    return render(request,'about.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data)
    data=data.text
    return render(request,'homepage.html',{'data' :data})
