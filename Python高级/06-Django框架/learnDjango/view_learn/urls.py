from django.urls import re_path, path
from .views import index, url

app_name = 'view'

urlpatterns = [
    re_path(r'^index$', index, name='view'),
    re_path(r'^url/(\d+)/(\d+)$', url)

]
