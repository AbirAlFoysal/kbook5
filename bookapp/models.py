from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from ckeditor.fields import RichTextField
from django.urls import reverse, reverse_lazy
from postapp.models import Post


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
    likes = models.ManyToManyField(User, related_name='bookapp_books')


    def __str__(self):
        return self.title

class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_book


class Comment(models.Model): 
	book = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = RichTextField(blank=True, null=True)
	data_added = models.DateField(auto_now_add=True)
	return_id = models.CharField(max_length=500, default=0)
	def __str__(self):
		return '%s - %s' %(self.book.title, self.name)
	def get_absolute_url(self):
		return reverse('book-detail', args=(str(self.return_id)))	
