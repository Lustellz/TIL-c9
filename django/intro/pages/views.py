from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request,'index.html')
    
#Template variables
def dinner(request):
    menu=["spagetti","hamberger","chicken","sushi","tofu","soup"]
    pick=random.choice(menu)
    
    return render(request,'dinner.html',{'dinner':pick})
    
#Variable routing
def hello(request,name):
    return render(request,'hello.html',{'name':name})
    
#Form tag
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message=request.GET.get('message')
    return render(request,'catch.html',{'message':message})
    
#Form request to external page
def naver(request):
    return render(request,'naver.html')
    
#Bootstrap
def bootstrap(request):
    return render(request,'bootstrap.html')