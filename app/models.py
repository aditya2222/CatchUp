from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
	CurrentUser = models.CharField(max_length=120,blank=True,null=True,editable=False)
	Title = models.CharField(max_length=120)
	Description = models.TextField()



	def __str__(self):
		return self.Title