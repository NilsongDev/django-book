from django.urls import include, path
from . import views





urlpatterns = [

    path('', views.book_view, name='inicio'),
    
]