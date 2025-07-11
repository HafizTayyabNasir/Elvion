from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TimeSlot, Appointment
from django.utils import timezone

@login_required
def book_appointment_view(request):
    available_slots = TimeSlot.objects.filter(is_booked=False, start_time__gte=timezone.now())

    if request.method == 'POST':
        slot_id = request.POST.get('time_slot')
        service_type = request.POST.get('service_type')
        notes = request.POST.get('notes')

        if not slot_id or not service_type:
            messages.error(request, "Please select a time slot and a service type.")
            return redirect('book_appointment')

        try:
            slot_to_book = TimeSlot.objects.get(id=slot_id, is_booked=False)

            Appointment.objects.create(
                user=request.user,
                time_slot=slot_to_book,
                service_type=service_type,
                notes=notes
            )

            slot_to_book.is_booked = True
            slot_to_book.save()

            messages.success(request, f"Your appointment for {slot_to_book} has been confirmed!")
            return redirect('dashboard')

        except TimeSlot.DoesNotExist:
            messages.error(request, "This time slot is no longer available. Please choose another.")
            return redirect('book_appointment')

    context = {
        'available_slots': available_slots
    }
    return render(request, 'appointments/get_your_appointment.html', context)


@login_required
def dashboard_view(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('time_slot__start_time')
    context = {
        'appointments': user_appointments,
        'now': timezone.now()
    }
    return render(request, 'appointments/dashboard.html', context)


@login_required
def cancel_appointment_view(request, appointment_id):
    appointment_to_cancel = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    
    if request.method == 'POST':
        appointment_to_cancel.status = 'CANCELLED'
        appointment_to_cancel.save()

        time_slot = appointment_to_cancel.time_slot
        time_slot.is_booked = False
        time_slot.save()

        messages.success(request, "Your appointment has been successfully cancelled.")
        return redirect('dashboard')
    
    return redirect('dashboard')