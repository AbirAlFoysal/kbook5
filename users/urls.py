from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views
urlpatterns = [
	
	path('register/', UserRegisterView.as_view(), name='register'),
	path('login_user', views.login_user, name='login2'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	#path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
	path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'),name='changepass'),
	path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page'),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('logout', views.logout_user, name = 'logout')

]
