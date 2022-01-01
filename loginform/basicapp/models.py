from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class UserProfileInfo(models.Model): 
# Create relationship (don't inherit from User!) 
    user = models.OneToOneField(User,on_delete= any) 
 
# Add any additional attributes you want 
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) 
    def __str__ (self):
     # Built—in attribute of django.contrib.auth.models.User !
        return self.user.username 
