from django.shortcuts import render,redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

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
    return render(request, 'movies/create.html', {'movie_form':form})
    
def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})