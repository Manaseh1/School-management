from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class NewUser(AbstractUser):
    Role = [
        ("A",'admin'),
        ("S",'student')
    ]
    reg_no = models.CharField(max_length=100,unique =True)
    # is_admin = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Role)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES,null=True,default=None)
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.OneToOneField(NewUser,on_delete= models.CASCADE)
    image = models.ImageField(upload_to="profile",default='default.png')
    phone = PhoneNumberField(blank=True)
    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name
    
class School(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Course(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100,unique = True)
    def __str__(self):
        return self.course_name   
class Units(models.Model):
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    unit_code = models.CharField(max_length =10)
    unit_name = models.CharField(max_length=100)
    def __str__(self):
        return self.unit_name

#This form will take in the details of registration
class CourseRegistration(models.Model):
    user = models.OneToOneField(NewUser,on_delete=models.CASCADE,default = None,unique=True)
    chosen_course = models.CharField(max_length=100)
    def __str__(self):
        return self.user.first_name