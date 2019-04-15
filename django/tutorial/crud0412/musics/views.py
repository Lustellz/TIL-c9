from django.shortcuts import render
from .models import Music

# Create your views here.

def singer_list(request):
    musics = Music.objects.all()
    return render(request, 'musics/singer_list.html', {'musics':musics})