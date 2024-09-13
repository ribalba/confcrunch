from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.conference_detail, name='conference_detail'),
    path('<slug:slug>/rate/', views.submit_rating, name='submit_rating'),
]
