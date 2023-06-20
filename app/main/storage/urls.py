from django.urls import path

from .views import upload_test_view, get_protected_file


urlpatterns = [
    path('upload/', upload_test_view),
    path('get_media/{id}', get_protected_file),
]
