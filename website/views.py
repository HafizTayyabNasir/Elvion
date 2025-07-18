from django.core import management
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import ContactMessage
import os
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Page Views
def home_view(request):
    return render(request, 'website/home.html')

def about_us_view(request):
    return render(request, 'website/about_us.html')

def services_view(request):
    return render(request, 'website/services.html')

def get_appointment_page_view(request):
    return render(request, 'website/get_your_appointment.html')
    
def contact_us_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message_text
        )
        messages.success(request, "Thank you for your message! We will get back to you shortly.")
        return redirect('contact_us')
    return render(request, 'website/contact_us.html')

# Authentication Views
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'website/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# ==============================================================================
# FINAL, CORRECT SECRET SUPERUSER CREATION VIEW
# ==============================================================================
# We renamed this in the urls.py to 'create_superuser_secret_view' but the original name was 'create_superuser_view'.
# Let's use the name from urls.py for consistency.