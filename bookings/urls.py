from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='bookings/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Built-in view
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('my-appointments/', views.user_appointments, name='user_appointments'),
    path('cancel/<int:pk>/', views.cancel_appointment, name='cancel_appointment'),
    path('welcome/',views.welcome,name='welcome')
]