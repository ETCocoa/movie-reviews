from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie


# Create your views here.
class MovieList(generic.ListView):
    queryset = Movie.objects.all().filter(status=1)
    template_name = "home/index.html"
    paginate_by = 6


def movie_detail(request, slug):
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    reviews = movie.reviews.all().order_by("-created_on")
    review_count = movie.reviews.filter(approved=True).count()

    return render(
        request,
        "home/movie_detail.html",
        {
        "movie": movie,
        "reviews": reviews,
        "review_count": review_count,
    },
    )
