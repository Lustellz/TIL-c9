from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.TextField()
    
#Doctor:Patient = 1:N
class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor, related_name = 'patients')
    
#Doctor:Reservation = 1:N -> Reservation = N*Doctor
#Patient:Reservation = 1:M -> Reservation = M*Patient
#N*Doctor = M*Patient -> M:N = Doctor:Patient
#Doctor:Patient = M:N
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

