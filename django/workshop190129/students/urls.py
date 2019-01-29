from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.Index),
    path('Create/',views.Create),
    path('New/',views.New),
    path('<int:student_id>/',views.Read),
    path('<int:student_id>/Delete/',views.Delete),
    path('<int:student_id>/Edit/',views.Edit),
    path('<int:student_id>/Update/',views.Update),
]