# elvion_project/urls.py
from django.contrib import admin
from django.urls import path, include
# Import the correctly named view
from website.views import create_superuser_secret_view 

urlpatterns = [
    # Use the correctly named view
    path('create-my-admin-now-and-forever-12345/', create_superuser_secret_view, name='create_admin'),
    
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('appointments/', include('appointments.urls')),
]