# inputbook/views.py
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



@login_required
def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inputbook')
    else:
        form = BookForm()
    return render(request, 'form/form.html', {'form': form})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'inputbook/book_list.html', {'books': books})



def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inputbook')
    else:
        form = AuthenticationForm()
    return render(request, 'form/login.html', {'form': form})