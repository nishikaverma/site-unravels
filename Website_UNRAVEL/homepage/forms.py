from django import forms
from .models import Suggessions

class SuggessionForm(forms.ModelForm):
    class Meta:
        model = Suggessions
        fields = ['name','email','suggession']
        lables =  {'name':'Name','suggession' :"Your Suggession"}
        widgets = {
          'suggession': forms.Textarea(attrs={'rows':5, 'cols':15}),
        }
        