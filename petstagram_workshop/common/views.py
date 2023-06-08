from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram_workshop.common.models import Like
from petstagram_workshop.photos.models import Photo


# Create your views here.


def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    like_objects = Like.objects.filter(to_photo_id=photo_id).first()

    if like_objects:
        like_objects.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details-photo', photo_id,))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
