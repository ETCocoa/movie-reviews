from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Movie
from .forms import ReviewForm


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
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.movie = movie
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Review submitted and awaiting approval"
            )
    
    review_form = ReviewForm()

    return render(
        request,
        "home/movie_detail.html",
        {
            "movie": movie,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )
