from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
def create(request):
    if request.method=='POST':
        form=ArticleModelForm(request.POST) #데이터를 넘길 때 /페이지를 넘길 때: form
        if form.is_valid():
            article=form.save()
            
            # title=request.POST.get('title') #검증되지 않은 값
            # content=request.POST.get('content')
            
            # title=form.cleaned_data.get('title') #검증된 값
            # content=form.cleaned_data.get('content')
            
            # article=Article.objects.create(title=title,content=content)
            
            #article=Article(title=title,content=content)
            #article.save()
            
            return redirect('articles:detail',article.pk)
        
    else:
        form=ArticleModelForm()
    return render(request, 'form.html',{'form':form})
        
def detail(request, article_id):
    article=Article.objects.get(pk=article_id)
    return render(request,'detail.html',{'article':article})
    
def update(request, article_id):
    article=Article.objects.get(pk=article_id)
    if request.method=='POST':
        form=ArticleModelForm(request.POST,instance=article)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail',article.pk)
    else:
        form=ArticleModelForm(instance=article)
    return render(request, 'form.html',{'form':form})
    
