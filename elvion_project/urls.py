# elvion_project/urls.py
from django.contrib import admin
from django.urls import path, include
# Add this new import
from website.views import setup_production_database

urlpatterns = [
    # THIS IS THE SECRET URL
    path('setup-my-live-database-and-admin-12345/', setup_production_database, name='setup_prod'),
    
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('appointments/', include('appointments.urls')),
]