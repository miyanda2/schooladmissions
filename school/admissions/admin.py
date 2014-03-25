from django.contrib import admin

# Register your models here.
from admissions.models import ApplicationFormTemplate


class ApplicationFormTemplateAdmin(admin.ModelAdmin):
    model = ApplicationFormTemplate


admin.site.register(ApplicationFormTemplate, ApplicationFormTemplateAdmin)
