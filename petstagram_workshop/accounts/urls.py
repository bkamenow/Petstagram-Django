from django.urls import path, include

from petstagram_workshop.accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register user'),
    path('login/', views.UserLoginView.as_view(), name='login user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', views.UserDetailsView.as_view(), name='profile details'),
        path('edit/', views.UserEditView.as_view(), name='profile edit'),
        path('delete/', views.UserDeleteView.as_view(), name='profile delete'),
    ]))
]
