from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from admissions.models import AppFormTemplateParameters, UserProfile, AppForm, Institution

admin.site.unregister(User)


class AppFormTemplateParametersAdmin(admin.StackedInline):
    model = AppFormTemplateParameters
    extra = 1
    max_num = 1


class AppFormAdmin(admin.ModelAdmin):
    model = AppForm
    inlines = [AppFormTemplateParametersAdmin]


class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

class InstitutionAdmin(admin.ModelAdmin):
    model = Institution

#admin.site.register(AppFormTemplateParameters, AppFormTemplateParametersAdmin)
admin.site.register(AppForm, AppFormAdmin)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Institution, InstitutionAdmin)
