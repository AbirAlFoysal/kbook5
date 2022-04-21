from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	website_url = models.CharField(max_length=255, blank=True,null=True)
	facebook_url = models.CharField(max_length=255, blank=True,null=True)
	instagram_url = models.CharField(max_length=255, blank=True,null=True)
	# post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)


	def get_absolute_url(self):
		return reverse('show_profile_page', args=(str(self.id)))
		#return reverse('home')

	def __str__(self):
		return str(self.user)
