from django.urls import re_path
from .views import index, book_info

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^book$', book_info)
]