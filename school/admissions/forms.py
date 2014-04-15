# EXAMPLE - formModel
# class InstitutionModelForm(forms.ModelForm):
#     class Meta:
#         model = m.Post
#         widgets = {
#             'content': forms.Textarea(attrs={'cols': 80, 'rows': 20})
#         }
from django.forms import ModelForm
from admissions.models import Institution, AppForm


class InstitutionModelForm(ModelForm):
    class Meta:
        model = Institution
        # widgets = {
        #     'content': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        # }


class AppFormForm(ModelForm):
    class Meta:
        model = AppForm


