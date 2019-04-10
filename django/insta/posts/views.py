from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.

def list(request):
    posts = Post.objects.order_by('-id').all()
    return render(request, 'posts/list.html', {'posts': posts})

@login_required

def create(request):
    if request.method == 'POST':
        # request.POST <-{'content':'asdf', 'user_id':1} 이런 상태임
        #요청에 사용자 정보가 포함되어 있으면 악용될 수 있음
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.user = request.user
            post.save() #실제 데이터베이스에 저장
            return redirect('posts:list')
    else:
        post_form = PostForm()
    return render(request, 'posts/form.html', {'post_form': post_form})
    
def update(request,post_id):
    post = get_object_or_404(Post, id = post_id)
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method =='POST':
        post_form = PostForm(request.POST, request.FILES, instance = post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/form.html',{'post_form':post_form})

def delete(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post=get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    # if post.user == request.user:
    #   post.delete()
    post.delete()
    return redirect('posts:list')