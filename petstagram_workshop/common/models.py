from django.db import models

from petstagram_workshop.accounts.models import PetstagramUser
from petstagram_workshop.photos.models import Photo


# Create your models here.

class Comment(models.Model):
    comment = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(PetstagramUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(PetstagramUser, on_delete=models.CASCADE)
