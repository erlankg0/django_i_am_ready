from django.urls import path
from .views import current_datetime, upload_file, get_name, mail

app_name = 'blog'
urlpatterns = [
    path('', current_datetime, name='datetime'),
    path('upload/', upload_file, name='upload'),
    path('name/', get_name, name='get_name'),
    path('contact/', mail, name='contact'),
]
