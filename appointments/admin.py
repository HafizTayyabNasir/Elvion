from django.contrib import admin
from .models import TimeSlot, Appointment

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'is_booked')
    list_filter = ('is_booked', 'start_time')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_slot', 'service_type', 'status', 'booked_at')
    list_filter = ('status', 'service_type', 'time_slot__start_time')
    search_fields = ('user__username', 'service_type')
    raw_id_fields = ('user', 'time_slot')