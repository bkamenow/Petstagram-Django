from django.shortcuts import render, redirect

from petstagram_workshop.common.forms import CommentForm
from petstagram_workshop.pets.models import Pet
from petstagram_workshop.pets.forms import PetFrom, PetDeleteForm


# Create your views here.


def add_pet(request):
    form = PetFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile details', pk=1)
    context = {'form': form}

    return render(request, template_name='pets/pet-add-page.html', context=context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photo = pet.photo_set.all()
    comment_form = CommentForm()
    context = {
        'pet': pet,
        'all_photos': all_photo,
        'comment_form': comment_form,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetFrom(instance=pet, initial=pet.__dict__)
    else:
        form = PetFrom(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details', username, pet_slug)
    context = {'form': form}

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}

    return render(request, template_name='pets/pet-delete-page.html', context=context)
