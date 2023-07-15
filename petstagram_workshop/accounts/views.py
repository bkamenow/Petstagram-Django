from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.views.generic import DeleteView

from petstagram_workshop.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
from petstagram_workshop.accounts.models import PetstagramUser
from petstagram_workshop.pets.models import Pet


# Create your views here.


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    form_clas = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


class UserDetailsView(views.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())
        total_photos = self.object.photo_set.count()
        total_pets = self.object.pets.count()

        context.update({
            'total_likes_count': total_likes_count,
            'total_photos': total_photos,
            'total_pets': total_pets,
        })
        return context


class UserEditView(views.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = PetstagramUser
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home page')

    def get_object(self, queryset=None):
        return self.request.user
