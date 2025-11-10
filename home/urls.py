from . import views
from django.urls import path


urlpatterns = [
    path("", views.MovieList.as_view(), name="home"),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
]
