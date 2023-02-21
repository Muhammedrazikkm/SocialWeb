from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Posts(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_name

class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="pic",null=True)
    bio=models.CharField(max_length=200)
    time_line_pic=models.ImageField(upload_to="pic",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)