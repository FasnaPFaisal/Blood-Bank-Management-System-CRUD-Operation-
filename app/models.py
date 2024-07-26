from django.db import models

# Create your models here.
class Donate(models.Model):
    GENDER_CHOICES = [
        ('', '--Select Gender--'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    BLOOD_GROUP_CHOICES = [
        ('', '--Select Blood Group--'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),        
    ]
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    mobile_number = models.IntegerField()
    email_id = models.EmailField(max_length=254)    
    photo = models.ImageField(upload_to='images/')


