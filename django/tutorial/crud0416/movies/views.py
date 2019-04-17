from django.shortcuts import render

# Create your views here.

def hello(a):
    return render(a, 'hello.html', {})
    
def hi(req, this):
    print(this)
    return render(req, 'hello.html', {'that' : this})