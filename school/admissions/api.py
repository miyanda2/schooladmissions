from django.contrib.auth.models import User
from admissions.models import Institution, AppForm
from tastypie.resources import ModelResource
from tastypie import fields


class InstitutionResource(ModelResource):

    class Meta:
        queryset = Institution.objects.all()
        resource_name = 'institution'
        #excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']


class AppFormResource(ModelResource):
    institute_id = fields.ForeignKey(InstitutionResource, 'institution')
    class Meta:
        queryset = AppForm.objects.all()
        resource_name = 'appform'
        allowed_methods = ['get']
