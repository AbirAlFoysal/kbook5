from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class createprofile(forms.ModelForm):
    profile_pic = forms.ImageField(required = False)
    bio = forms.CharField(max_length=1500, required = False)
    phone = forms.IntegerField(required = False)
    website = forms.URLField(required = False)
    facebook = forms.URLField(required = False)
    instagram = forms.URLField(required = False)
    college = forms.CharField(max_length=250, required = False)
    school = forms.CharField(max_length=250, required = False)

    

    class Meta:
        model = Profile
        fields = ['bio',
        'profile_pic',
        'phone',
        'website', 
        'facebook', 
        'instagram',
        'college',
        'school',
        ]


class usercreate(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    department = forms.CharField(max_length=6, required = True)
    batch = forms.CharField(max_length=4, required = True)
    hometown = forms.CharField(max_length=250, required = False)

    class Meta:
        model = User
        fields = ['username', 'department','batch','hometown', 'email', 'password1', 'password2']


class userupdtate(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']



class UpdateProfile(forms.ModelForm):
    bio = forms.CharField(max_length=1500, required = False)
    phone = forms.IntegerField(required = False)
    website = forms.URLField(required = False)
    facebook = forms.URLField(required = False)
    instagram = forms.URLField(required = False)
    college = forms.CharField(max_length=250, required = False)
    school = forms.CharField(max_length=250, required = False)
    batch = forms.CharField(max_length=4)


    

    class Meta:
        model = Profile
        fields = ['bio',
        'profile_pic',
        'phone',
        'website', 
        'facebook', 
        'instagram',
        'college',
        'school',
		'batch',
        ]

class PasswordChangingForm(PasswordChangeForm):


	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')
			
