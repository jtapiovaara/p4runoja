from django import forms
from.models import RunoDB

class RunoForm(forms.ModelForm):
    class Meta:
        model = RunoDB
        fields = {'name',
                  'caption',
                  'author'
                  }