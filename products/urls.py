from django.urls import path
from .views import index, my_list, practice, pris, file, address, test, repetit

urlpatterns = [
    path('', index),
    path('list/', my_list),
    path('about/', practice),
    path('tutorials/', pris),
    path('folder/', file),
    path('learn/', address),
    path('test/', test),
    path('repetit/', repetit)
]