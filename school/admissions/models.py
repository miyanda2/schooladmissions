from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from separatedvaluesfield.models import SeparatedValuesField

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

RELATIONSHIP = (
    ('F', 'Father'),
    ('M', 'Mother'),
    ('B', 'Brother'),
    ('S', 'Sister'),
    ('G', 'Guardian'),
)

DEGREES = (
    ('B.Sc', 'B.Sc'),
    ('PUC', 'PUC'),
    ('10th Std', '10th STD'),
    ('12th Std', '12th STD'),
    ('B.Comm', 'B.Comm'),
)


# Refer here for details avout SeparatedValuesField: https://github.com/thoas/django-separatedvaluesfield
class Institution(models.Model):
    #define your columns here
    institute_id = models.IntegerField(auto_created=True, primary_key=True, editable=False, help_text="Institution ID")
    name = models.CharField(max_length=200, blank=False, null=False, db_index=True, editable=True,
                            verbose_name='Institution Name', help_text='Institution Name. Users will search by name.')
    address = models.CharField(max_length=200, blank=False, null=False, db_index=False, editable=True,
                               verbose_name='Address',
                               help_text='Site No, Street Name and other address related details')
    city = models.CharField(max_length=100, blank=False, null=False, db_index=False, editable=True,
                            verbose_name='City', help_text='City')
    state = models.CharField(max_length=50, blank=False, null=False, db_index=False, editable=True,
                             verbose_name='State', help_text='State')
    start_class_level = models.CharField(max_length=20, blank=False, null=False, db_index=False, editable=True,
                                         verbose_name='Starting class level',
                                         help_text='State the lowest class level at which kids can get admitted to the institution')
    end_class_level = SeparatedValuesField(max_length=200, blank=False, null=False, db_index=False, editable=True,
                                           choices=DEGREES, verbose_name='Highest class level',
                                           help_text='State the highest class level till which students can study in the institute')

    class Meta:
        verbose_name_plural = 'Institutions'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('view-institute-details', kwargs={'institute_id': str(self.pk)})

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.name, self.address, self.state)


# Create your models here.
# ********* NOTE: TO-DO *********************
# If you add any more columns to this model, then  make sure to delete the db and run syncdb again.
# Since there is the 'admin' account created, any column changes need the DB to be recreated. Maybe there is a proper solution to this, but needs
# to be investigated.
#*************************************
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    description = "Stores additional details about a user"

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone = models.IntegerField(max_length=10, unique=False, validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    sex = models.CharField(max_length=1, blank=True, null=True, db_index=False, editable=True, choices=GENDER_CHOICES,
                           verbose_name='Sex', help_text='Sex')
    nationality = models.CharField(max_length=20, blank=True, null=True, db_index=False, editable=True,
                                   verbose_name='Nationality', help_text='Nationality (Ex: Indian)')
    religion = models.CharField(max_length=20, blank=True, null=True, db_index=False, editable=True,
                                verbose_name='Religion', help_text='Religion (Ex: Hindu)')
    mother_tongue = models.CharField(max_length=20, blank=True, null=True, db_index=False, editable=True,
                                     verbose_name='Mother Tongue', help_text='Mother Tongue (Ex: Kannada)')
    community = models.CharField(max_length=20, blank=True, null=True, db_index=False, editable=True,
                                 verbose_name='Community', help_text='Community (Ex: ST or SC or OBC or Others)')
    #Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


# Create your models here.
class UserFamilyProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50, blank=False, null=False, db_index=False, editable=True,
                                  verbose_name='First Name', help_text='First Name')
    last_name = models.CharField(max_length=50, blank=True, null=True, db_index=False, editable=True,
                                 verbose_name='Last Name', help_text='Last Name')
    relationship = models.CharField(max_length=1, blank=False, null=False, db_index=False, editable=True,
                                    choices=RELATIONSHIP,
                                    verbose_name='Relationship', help_text='Relationship')
    annual_income = models.CharField(max_length=1, blank=False, null=False, db_index=False, editable=True,
                                     choices=RELATIONSHIP,
                                     verbose_name='Annual Income', help_text='Annual Income (Ex: 10 Lakhs)')

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


# Basic application form that holds all the application related parameters
class AppForm(models.Model):
    #define your columns here
    appform_id = models.IntegerField(auto_created=True, name='Application Form ID', primary_key=True, editable=False, )
    name = models.CharField(max_length=100, blank=False, null=False, db_index=True, editable=True,
                            verbose_name='Name of the application form',
                            help_text='Name of the application form')
    description = models.CharField(max_length=400, blank=True, null=True, db_index=False, editable=True,
                                   verbose_name='Description of the form',
                                   help_text='Description of the application form')
    institute_id = models.ForeignKey(Institution)
    class Meta:
        verbose_name_plural = "Application Forms"

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return 'Application Form: {0}.  {1}'.format(self.name, self.description)


#Application form template parameters that stores boolean flags for each of the possible form fields
class AppFormTemplateParameters(models.Model):
    #each of the boolean flags are listed below
    app_form_id = models.ForeignKey(AppForm)
    is_visible_first_name = models.BooleanField(default=True, verbose_name='First Name', editable=False,
                                                help_text='Displays first name field on the form')
    is_visible_last_name = models.BooleanField(default=True, editable=False, verbose_name='Middle Name',
                                               help_text='Displays last name field on the form')

    is_visible_middle_name = models.BooleanField(default=True, verbose_name='Middle Name',
                                                 help_text='Need to show middle name field on the form ?')

    is_visible_father_name = models.BooleanField(default=True)
    is_visible_mother_name = models.BooleanField(default=True)
    is_visible_address = models.BooleanField(default=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return 'Application Form Template for userd id = {0}'.format(self.app_form_id)

