from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_us_view, name='about_us'),
    path('about-us/', views.about_us_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('contact/', views.contact_us_view, name='contact_us'),
    
    path('get-your-appointment/', views.get_appointment_page_view, name='get_appointment_page'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]