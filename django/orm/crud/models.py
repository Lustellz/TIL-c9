from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField()
    
#class Post: django에서는 model, db에서는 table
#post = Post(): class를 instance화. django에서는 instance 혹은 object(OOP의 개념), db에서는 record 혹은 row
#title: django에서는 Field, db에서는 column

#CRUD
#1. Create를 할 수 있는 방법
#post = Post(title = 'hello-1')
#post.save()

#post2 = Post.objects.create(title='hello-2')

#post3 = Post()
#post3.title = 'hello-3'
#post3.save()
#post3.title = 'hello!!'로 바로 수정 할 수 있음

#2. Read를 할 수 있는 방법
#모든 값을 불러올 때
#posts = Post.object.all()

#하나의 값을 불러올 때
#post = Post.objects.get(pk=1) id = 1, title='hello-1'도 가능
#views.py 한정으로
#from django.shortcuts import get_objects_or_404
#post = get_object_or_404(Post, pk=1) id = 1, title = 'hello-1'도 가능
#post = Post.objects.filter(pk=1)[0] id = 1, title = 'hello-1'도 가능
#post = Post.objects.filter(pk=1).first()
#where(filter)
#posts = Post.objects.filter(title='hello-1')
#post = Post.objects.filter(title='hello-1').first() 또는 [0]

#like
#posts = Post.objects.filter(title__contains = 'lo')

#order_by
#posts = Post.objects.order_by('title') 제목 오름차순
#posts = Post.objects.order_by('-title') 제목 내림차순

#offset & limit
#post = Post.objects.all()[0] offset: 앞쪽에 몇 개를 제외시킬 것인지(현재는 offset 0, limit 1인 상태)
#Post.objects.all()[0] : 현재 offset 0, limit 1
#Post.objects.all()[1] : 현재 offset 1, limit 1
#Post.objects.all()[1:3] : 현재 offset 1, limit 2
#Post.objects.all()[offset:offset+limit]

#3. Update
#post = Post.objects.get(pk=1)
#post.title = 'hello-5'
#post.save() 실제 데이터베이스에 저장

#4. Delete
#post = Post.objects.get(pk=1)
#post.delete()
#한 줄로 표현: Post.objects.get(pk=1).delete()