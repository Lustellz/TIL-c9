from django.urls import path, include

app_name = 'musics'

urlpatterns = [
    path('', views.singer_list, name='singer_list'),
    ]