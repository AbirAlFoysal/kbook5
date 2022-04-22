from django.shortcuts import render, redirect
from .models import Book, Category, Comment
from django.views.generic import CreateView
# from  .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect



# Create your views here.
def bookhome(request):
    recommended_books = Book.objects.filter(recommended_books = True)
    fiction_books = Book.objects.filter(fiction_books = True)
    business_books = Book.objects.filter(business_books = True)
    return render(request, 'bookhome.html', {'recommended_books': recommended_books,
    'business_books': business_books, 'fiction_books': fiction_books
    })

def all_books(request):
    books = Book.objects.all()

    return render(request, 'all_books.html', {'books':books})

def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    return render(request, 'genre_detail.html', {'category': category})

@login_required(login_url='login2')
def book_detail(request, slug):
    book = Book.objects.get(slug = slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith = book_category)
    return render(request, 'book_detail.html', {'book': book, 'similar_books': similar_books})

def search_book(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, 'search_book.html', {'searched_books':searched_books})


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = "__all__"


	def form_valid(self, form):
		form.instance.book_id = self.kwargs['pk']
		form.instance.name = self.request.user.username
		form.instance.return_id = self.kwargs['pk']
		return super().form_valid(form)


def LikeView(request, pk):
		book = get_object_or_404(Book, id=request.POST.get("book_id"))
		liked = False
		if book.likes.filter(id=request.user.id).exists():
			book.likes.remove(request.user)
			liked = False
		else:	
			book.likes.add(request.user)
			liked = True
		return HttpResponseRedirect(reverse('book-detail',args=[str(pk)]))

