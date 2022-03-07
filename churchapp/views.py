from django.shortcuts import render

# Create your views here.

# Create your views here.  
from django.http import HttpResponse
from django.template import loader
from churchapp.form import SubForm
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def susbscribers(request):
    return HttpResponse("<h2>Welcome to Subscribers page!</h2>")

def index(request):  
   #template = loader.get_template('index.html') # getting our template  
   # HttpResponse(template.render())       # rendering the template in HttpResponse

   sub = SubForm()
   return render(request,"index.html",{'form':sub})