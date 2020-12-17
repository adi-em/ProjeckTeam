from django import forms
from adminapp.models import dataguru, datamurid

class imgform(forms.ModelForm):
    class Meta():
         model = datamurid
         fields = ('__all__')