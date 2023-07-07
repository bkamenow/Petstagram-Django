from django import forms

from petstagram_workshop.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        }
        labels = {
            'description': 'Description',
            'location': 'Location',
        }
        exclude = {'user'}


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']
