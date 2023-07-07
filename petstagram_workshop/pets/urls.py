from django.urls import path, include

from petstagram_workshop.pets import views

urlpatterns = [
    path('add/', views.CreatePetView.as_view(), name='add-pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', views.DetailsPetView.as_view(), name='details-pet'),
        path('edit/', views.EditPetView.as_view(), name='edit-pet'),
        path('delete/', views.DeletePetView.as_view(), name='delete-pet'),

    ]))
]
