# inputbook/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_book, name='inputbook'),  # Cambia 'inputbook/' por ''
    path('books/', views.list_books, name='list_books'),
]