from django import forms
from .models import Links


class Link_form(forms.ModelForm):
    original_url = forms.URLField(label='')
    class Meta:
        model = Links
        fields = ('original_url',)