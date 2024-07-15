from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("details/<str:id>/", views.details, name="details"),
    path("search/", views.search, name="search"),
    path("signup/", views.signup, name="signup"),
]
