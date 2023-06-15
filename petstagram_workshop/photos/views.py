from django.shortcuts import render, redirect

from petstagram_workshop.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram_workshop.photos.models import Photo


# Create your views here.


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context = {'form': form}

    return render(request, template_name='photos/photo-add-page.html', context=context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comment = photo.comment_set.all()
    context = {
        'photos': photo,
        'likes': likes,
        'comments': comment,
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details-photo', pk=pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home page')
