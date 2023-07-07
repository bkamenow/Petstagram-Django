from django.db import models
from django.template.defaultfilters import slugify

from petstagram_workshop.accounts.models import PetstagramUser
from petstagram_workshop.photos.validators import validate_file_size


# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0, blank=True)
    type = models.CharField(max_length=12, blank=True)
    personal_photo = models.ImageField(upload_to='media/', blank=True, validators=(validate_file_size,))
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)
    user = models.ForeignKey(PetstagramUser, related_name='pets', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.type}'
