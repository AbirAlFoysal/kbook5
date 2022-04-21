from django.db import models
from django.contrib.auth.models import User
from users.models import Profile


# Create your models here.
class Category(models.Model):
    name = models.CharField('Categories', max_length=50)
    slug = models.SlugField(max_length = 50)
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100)
    cover_image = models.ImageField(upload_to = 'img', blank = True, null = True)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    recommended_books = models.BooleanField(default=False)
    fiction_books = models.BooleanField(default=False)
    business_books = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_book
