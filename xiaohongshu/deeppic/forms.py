from django import forms
from .models import LocalPics

class FileFieldForm(forms.Form):
    file_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UserPicSelection(forms.ModelForm):
    class Meta:
        model = LocalPics
        fields = ['imagelocal']