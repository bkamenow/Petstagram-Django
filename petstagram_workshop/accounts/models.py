from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_workshop.photos.validators import validate_file_size
from validators.validators import check_string_contains_only_letters


class PetstagramUser(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Other'),
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30,
                                  blank=True,
                                  validators=[
                                      MinLengthValidator(2),
                                      check_string_contains_only_letters
                                  ])
    last_name = models.CharField(max_length=30,
                                 blank=True,
                                 validators=[
                                     MinLengthValidator(2),
                                     check_string_contains_only_letters
                                 ])
    profile_picture = models.ImageField(upload_to='media/', blank=True, validators=(validate_file_size,))
    gender = models.CharField(choices=GENDER_CHOICES, blank=True)

    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username
