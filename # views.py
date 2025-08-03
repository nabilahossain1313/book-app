
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Book
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'sign_in.html')