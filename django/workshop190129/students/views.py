from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

def New(request):
    return render(request, 'New.html')
    
def Create(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    birthday=request.POST.get('birthday')
    age=request.POST.get('age')
 
    student=Student(name=name,email=email,birthday=birthday,age=age)
    student.save()
    
    return redirect(f'/students/{student.pk}/')

def Index(request):
    students=Student.objects.all()
    return render(request,'Index.html',{'students':students})
    
def Read(request, student_id):
    student=Student.objects.get(pk=student_id)
    return render(request,'Read.html',{'student':student})

def Delete(request, student_id):
    student=Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/students/')
    
def Edit(request,student_id):
    student=Student.objects.get(pk=student_id)
    return render(request,'Edit.html',{'student':student})
    
def Update(request,student_id):
    #수정하는 코드
    student=Student.objects.get(pk=student_id)
    student.name=request.POST.get('name')
    student.email=request.POST.get('email')
    student.birthday=request.POST.get('birthday')
    student.age=request.POST.get('age')
    student.save()
    
    return redirect(f'/students/{student_id}/')


# Create your views here.
