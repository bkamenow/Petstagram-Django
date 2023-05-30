from django.urls import path, include

from .views import register_user, login_user, show_profile_details, edit_profile, delete_profile

urlpatterns = [
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('profile/<int:pk>/', include([
        path('', show_profile_details, name='profile details'),
        path('edit/', edit_profile, name='profile edit'),
        path('delete/', delete_profile, name='profile delete'),
    ]))
]
