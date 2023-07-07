from django import forms

from petstagram_workshop.pets.models import Pet


class PetFrom(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'type', 'date_of_birth', 'personal_photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
            'type': forms.TextInput(attrs={'placeholder': 'Type'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.FileInput(),
        }
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Personal Photo',
        }


class PetDeleteForm(PetFrom):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.arttrs['disabled'] = 'disabled'
            field.widget.arttrs['readonly'] = 'readonly'
