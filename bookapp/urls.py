import imp
from django.urls import path
from . import views
from .views import LikeView, AddCommentView

urlpatterns = [
    path('general/', views.bookhome, name = 'bookhome'),
    path('all_books', views.all_books, name = 'all_books'),
    path('genre/<str:slug>', views.category_detail, name = 'category_detail'),
    path('pdf/<str:slug>', views.book_detail, name = 'book_detail'),
    path('searched_books', views.search_book, name = 'book_search'),
    # path('register', views.register_page, name = 'register'),
    # path('login', views.login_page, name = 'login'),
    # path('logout', views.logout_user, name = 'logout'),

	path('like/<int:pk>', LikeView, name="like_book"),
	path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),





]