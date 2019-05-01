from django.shortcuts import render,redirect, get_object_or_404
from .forms import MovieForm, CommentForm
from .models import Movie, Comment
from django.views.decorators.http import require_POST

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = MovieForm (request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('/movies/{}/'.format(movie.id))
            #return redirect('movies:detail', movie.id) #movie_id = movie.id
            #'movies:detail', movie.id => /movies/1/, movie_id = 1
    else:
        form = MovieForm()
    # movie_form = MovieForm()
    return render(request, 'movies/form.html', {'form':form})
    
def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = CommentForm()
    return render(request, 'movies/detail.html', {'movie':movie, 'form':form})
    
def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies':movies})
    
def update(request, movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    
    if request.method=='POST':
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie_id)
    else:
        form = MovieForm(instance=movie)    
    return render(request, 'movies/form.html', {'form':form})
    
@require_POST    
def delete(request, movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    movie.delete()
    return redirect('movies:list')
    
@require_POST
def comment_create(request, movie_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie_id = movie_id
        comment.save()
    return redirect('movies:detail', movie_id)
    
@require_POST
def comment_delete(request, movie_id, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    comment.delete()
    return redirect('movies:detail', movie_id)