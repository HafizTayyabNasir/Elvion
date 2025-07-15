# elvion_project/urls.py
from django.contrib import admin
from django.urls import path, include
from website.views import create_superuser_secret_view

urlpatterns = [
    # THIS LINE MUST BE HERE
    path('make-me-admin-now-and-forever-12345/', create_superuser_secret_view, name='create_admin'),
    
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('appointments/', include('appointments.urls')),
]