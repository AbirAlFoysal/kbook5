from django.shortcuts import render
from django.views import generic
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from flask_login import login_required
from django.contrib.auth.models import User
from .forms import UpdateProfile, createprofile, PasswordChangingForm, usercreate, userupdtate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, CreateView, DetailView
from postapp.models import Post, Comment
from .models import Profile
from django.views.decorators.csrf import csrf_exempt





class CreateProfilePageView(CreateView):
	model = Profile
	form_class = createprofile
	template_name = "registration/create_user_profile_page.html"
	#fields = ['bio' ,'profile_pic', 'website_url', 'facebook_url', 'instagram_url']
	#fields = '__all__'
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
	model = Profile
	form_class = UpdateProfile
	template_name = 'registration/edit_profile_page.html'  
	#fields = ['bio' ,'profile_pic', 'website_url', 'facebook_url', 'instagram_url']
	success_url = reverse_lazy('home')

	def form_valid(self, form):

		messages.success(self.request, 'Profile has been updated successfully”')
		return super().form_valid(form)




class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile_page.html'

	def get_context_data(self, *args, **kwargs):
		users = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs )
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context


class UserRegisterView(generic.CreateView):
	form_class = usercreate
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('login2')
	#success_message = "User was created successfully"


	def form_valid(self, form):

		messages.success(self.request, 'New user was created successfully”')
		return super().form_valid(form)


@csrf_exempt
def	login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, 'There was an error, try again.')
			return redirect('home')
	else:
		return render(request, 'registration/login2.html',{})		

class UserEditView(generic.UpdateView):
	form_class = userupdtate
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')
	#success_message = "User was created successfully"


	def form_valid(self, form):

		messages.success(self.request, "The profile has been updated .")
		return super().form_valid(form)		

	def get_object(self):
		return self.request.user	

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):

		messages.success(self.request, "The Password has been updated.")
		return super().form_valid(form)		




def logout_user(request):
    logout(request)
    return redirect('home')
    