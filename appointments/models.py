# appointments/models.py
from django.db import models
from django.conf import settings # To link to the User model

class TimeSlot(models.Model):
    """Represents a single available time slot for an appointment."""
    start_time = models.DateTimeField(unique=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        # Format: "July 9, 2025, 10:00 AM"
        return self.start_time.strftime("%B %d, %Y, %I:%M %p")

    class Meta:
        ordering = ['start_time']

class Appointment(models.Model):
    """Represents a booked appointment by a user."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CONFIRMED')

    def __str__(self):
        return f"Appointment for {self.user.username} at {self.time_slot}"

    class Meta:
        ordering = ['-time_slot__start_time']