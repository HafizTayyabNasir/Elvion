from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('appointments/', include('appointments.urls')),
]