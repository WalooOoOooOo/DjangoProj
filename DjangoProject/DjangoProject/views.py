# from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # return HttpResponse("Homepage")
    return render(request,'home.html')
def aboutpage(request):
    # return HttpResponse("AboutPage")
    return render(request,'about.html')