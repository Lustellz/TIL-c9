from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('<int:movie_id>/', views.detail, name='detail'),
    ]