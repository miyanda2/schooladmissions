from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


#Application form template that stores boolean flags for each of the possible form fields
class ApplicationFormTemplate(models.Model):
    #each of the boolean flags are listed below
    is_visible_first_name = models.BooleanField(default=True)
    is_visible_middle_name = models.BooleanField(default=True)
    is_visible_last_name = models.BooleanField(default=True)
    is_visible_father_name = models.BooleanField(default=True)
    is_visible_mother_name = models.BooleanField(default=True)
    is_visible_address = models.BooleanField(default=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return 'Application Form Template for userd id = '.format()


