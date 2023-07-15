from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views, generic

from petstagram_workshop.pets.models import Pet
from petstagram_workshop.pets.forms import PetFrom, PetDeleteForm


@method_decorator(login_required, name='dispatch')
class CreatePetView(views.CreateView):
    model = Pet
    form_class = PetFrom
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


class DetailsPetView(generic.DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_name'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username=self.kwargs['username'], slug=self.kwargs['pet_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.get_object()
        all_photos = pet.photo_set.all()
        context['all_photos'] = all_photos
        return context


@method_decorator(login_required, name='dispatch')
class EditPetView(views.UpdateView):
    model = Pet
    form_class = PetFrom
    template_name = 'pets/pet-edit-page.html'
    slug_field = 'slug'
    slug_url_kwarg = 'pet_name'

    def get_success_url(self):
        return reverse_lazy('details-pet', kwargs={'username': self.object.user.username, 'pet_name': self.object.slug})


@method_decorator(login_required, name='dispatch')
class DeletePetView(views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    slug_field = 'slug'
    slug_url_kwarg = 'pet_name'
    success_url = reverse_lazy('home page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
