from django.contrib import admin
from django.urls import path, include
# This is no longer needed
# from website.views import create_superuser_secret_view 

urlpatterns = [
    # The secret URL is removed. The superuser is now created in the build script.
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('appointments/', include('appointments.urls')),
]