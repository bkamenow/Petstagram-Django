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
    class Meta(PetFrom.Meta):
        exclude = ['personal_photo']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
        for field_name, field in self.fields.items():
            field.required = False
        if instance:
            self.initial.update({
                'name': instance.name,
                'age': instance.age,
                'type': instance.type,
                'date_of_birth': instance.date_of_birth,
            })
