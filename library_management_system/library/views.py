from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import AddBookForm, IssueBookForm, ReturnBookForm, AddMembershipForm, UserForm
from .models import Book, User, BookIssue
from datetime import datetime

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)  # Log the user in
                return redirect('dashboard')  # Redirect to the dashboard on successful login
            else:
                # If authentication fails, show an error message
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'library/login.html', {'form': form})

def dashboard(request):
    return render(request, 'library/dashboard.html')

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddBookForm()
    return render(request, 'library/add_book.html', {'form': form})

def add_member(request):
    if request.method == 'POST':
        form = AddMembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddMembershipForm()
    return render(request, 'library/add_member.html', {'form': form})

def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IssueBookForm()
    return render(request, 'library/issue_book.html', {'form': form})

def return_book(request):
    if request.method == 'POST':
        form = ReturnBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ReturnBookForm()
    return render(request, 'library/return_book.html', {'form': form})

def pay_fine(request):
    # Implement logic to handle fine payment
    return render(request, 'library/pay_fine.html')

def update_membership(request):
    if request.method == 'POST':
        form = AddMembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddMembershipForm()
    return render(request, 'library/update_membership.html', {'form': form})

def user_management(request):
    # Implement logic for user management
    return render(request, 'library/user_management.html')