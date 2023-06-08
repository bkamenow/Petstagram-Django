from django.urls import path

from .views import home_page, like_functionality, copy_link_to_clipboard

urlpatterns = [
    path('', home_page, name='home page'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),
]
