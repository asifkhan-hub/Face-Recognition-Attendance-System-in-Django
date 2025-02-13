# forms.py
from django import forms
from .models import UploadedImage

class UploadImageForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image', widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = UploadedImage
        fields = ['name', 'image']
