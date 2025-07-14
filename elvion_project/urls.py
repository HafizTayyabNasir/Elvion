from django.contrib import admin
from django.urls import path, include
from website.views import create_superuser_view 

urlpatterns = [
    # THIS IS THE SECRET URL TO CREATE YOUR ADMIN ACCOUNT
    path('create-my-admin-now-d7r4k9z/', create_superuser_view, name='create_admin'),
    
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('appointments/', include('appointments.urls')),
]