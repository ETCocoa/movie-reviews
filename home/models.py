from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    genres = models.ManyToManyField("Genre", related_name="movies", blank=True)
    length = models.PositiveIntegerField(help_text="Length in minutes")
    released = models.DateField()
    status = models.IntegerField(choices=STATUS, default=0)
    movie_image = CloudinaryField("image", default="placeholder")

    # Roles involved in movie
    directors = models.ManyToManyField("Person", related_name="directed_movies", blank=True)
    writers = models.ManyToManyField("Person", related_name="written_movies", blank=True)
    stars = models.ManyToManyField("Person", related_name="starred_movies", blank=True)

    class Meta:
        ordering = ["-released"]

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.author}"


class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
