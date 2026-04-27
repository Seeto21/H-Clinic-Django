from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('pediatrics', 'Pediatrics'),
        ('general', 'General Physician'),
        ('dentist','bds')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)
    
    def __str__(self):
        return f"Dr. {self.user.last_name}"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    timeslot = models.TimeField()
    is_confirmed = models.BooleanField(default=True)
    class Meta:
        unique_together = ('doctor', 'date', 'timeslot')