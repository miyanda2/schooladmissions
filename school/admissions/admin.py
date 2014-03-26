from django.contrib import admin

# Register your models here.
from admissions.models import AppFormTemplateParameters, UserProfile, AppForm, Institution


class AppFormTemplateParametersAdmin(admin.StackedInline):
    model = AppFormTemplateParameters
    extra = 1
    max_num = 1


class AppFormAdmin(admin.ModelAdmin):
    model = AppForm
    inlines = [AppFormTemplateParametersAdmin]


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

class InstitutionAdmin(admin.ModelAdmin):
    model = Institution

#admin.site.register(AppFormTemplateParameters, AppFormTemplateParametersAdmin)
admin.site.register(AppForm, AppFormAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Institution, InstitutionAdmin)
