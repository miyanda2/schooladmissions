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


class AppForm(models.Model):
    #define your columns here
    id = models.IntegerField(auto_created=True, name='Application Form ID', primary_key=True, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False, db_index=True, editable=True,
                            verbose_name='Name of the application form',
                            help_text='Name of the application form')
    description = models.CharField(max_length=400, blank=False, null=False, db_index=True, editable=True,
                                   verbose_name='Name of the application form',
                                   help_text='Name of the application form')

    class Meta:
        verbose_name_plural = "Application Forms"

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return 'Application Form Template for userd id = '.format()


#Application form template parameters that stores boolean flags for each of the possible form fields
class AppFormTemplateParameters(models.Model):
    #each of the boolean flags are listed below
    app_form_id = models.ForeignKey(AppForm)
    is_visible_first_name = models.BooleanField(default=True, verbose_name='First Name',
                                                help_text='Need to show first name field on the application form ?')
    is_visible_middle_name = models.BooleanField(default=True, verbose_name='Middle Name',
                                                 help_text='Need to show middle name field on the application form ?')
    is_visible_last_name = models.BooleanField(default=True)
    is_visible_father_name = models.BooleanField(default=True)
    is_visible_mother_name = models.BooleanField(default=True)
    is_visible_address = models.BooleanField(default=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return 'Application Form Template for userd id = {0}'.format(self.app_form_id)


class Institution(models.Model):
    #define your columns here
    id = models.IntegerField(auto_created=True, name='Institution ID', primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False, db_index=True, editable=True,
                            verbose_name='Institution Name', help_text='Institution Name. Users will search by name.')
    address = models.CharField(max_length=200, blank=False, null=False, db_index=False, editable=True,
                               verbose_name='Address',
                               help_text='Site No, Street Name and other address related details')
    city = models.CharField(max_length=100, blank=False, null=False, db_index=False, editable=True,
                            verbose_name='City', help_text='City')
    state = models.CharField(max_length=50, blank=False, null=False, db_index=False, editable=True,
                             verbose_name='State', help_text='State')

    class Meta:
        verbose_name_plural = "Institutions"

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return 'Institution'
