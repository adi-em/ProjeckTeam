from django import forms
from adminapp.models import dataguru

class imgform(forms.ModelForm):
    class Meta():
         model = dataguru
         fields = ('foto',)