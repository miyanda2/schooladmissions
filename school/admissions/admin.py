from django.contrib import admin

# Register your models here.
from admissions.models import AppFormTemplateParameters, UserProfile, AppForm


class AppFormAdmin(admin.ModelAdmin):
    model = AppForm


class AppFormTemplateParametersAdmin(admin.StackedInline):
    model = AppFormTemplateParameters


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

#admin.site.register(AppFormTemplateParameters, AppFormTemplateParametersAdmin)
admin.site.register(AppForm, AppFormAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
