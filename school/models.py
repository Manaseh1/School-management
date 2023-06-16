from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class NewUser(AbstractUser):
    Role = [
        ("A",'admin'),
        ("S",'student')
    ]
    reg_no = models.CharField(max_length=100, null = True)
    # is_admin = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Role,null=True)

class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES,null=True,default=None)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.OneToOneField(NewUser,on_delete= models.CASCADE)
    image = models.ImageField(upload_to="/profile",default='default.png')
    phone = PhoneNumberField(blank=True)

class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
class School(models.Model):
    name = models.CharField(max_length=100)
class Course(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
class Units(models.Model):
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    unit_code = models.CharField(max_length =10)
    unit_name = models.CharField(max_length=100)