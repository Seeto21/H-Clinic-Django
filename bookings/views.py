from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor, Appointment
from .forms import AppointmentForm

def home(request):
    bg = "https://images.unsplash.com/photo-1505751172107-573957a2482c"
    return render(request, 'bookings/home.html', {'bg_image': bg})


def welcome(request):
    return render(request, 'bookings/welcome.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'bookings/register.html', {'form': form})

@login_required(login_url='register')
def doctor_list(request):
    all_doctors = Doctor.objects.all()
    bg = "https://images.unsplash.com/photo-1559839734-2b71f1e3c770"
    # FIXED: Combined doctors and bg_image into ONE dictionary
    return render(request, 'bookings/doctor_list.html', {
        'doctors': all_doctors, 
        'bg_image': bg
    })

@login_required(login_url='register')
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('user_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'bookings/book_appointment.html', {'form': form})

@login_required(login_url='login')
def user_appointments(request):
    my_bookings = Appointment.objects.filter(patient=request.user).order_by('date')
    bg = "https://images.unsplash.com/photo-1505751172107-573957a2482c"
    # FIXED: Combined appointments and bg_image into ONE dictionary
    return render(request, 'bookings/user_appointments.html', {
        'appointments': my_bookings, 
        'bg_image': bg
    })

@login_required(login_url='login')
def cancel_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk, patient=request.user)
    except Appointment.DoesNotExist:
        return redirect('home')

    if request.method == "POST":
        appointment.delete()
        messages.warning(request, "Appointment cancelled.")
        return redirect('user_appointments')
    
    return render(request, 'bookings/cancel_confirm.html', {'appointment': appointment})