from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment_view, name='book_appointment'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment_view, name='cancel_appointment'),
]