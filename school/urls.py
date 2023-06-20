from django.urls import path
from .views import *
urlpatterns = [
    path('',register,name='signup'),
    path('signin/',signin,name ='signin'),
    path('profile/',profile,name ="profile"),
    path('logout',signout,name ='logout'),
    path('output/',example,name ='output'),
    path('addcourse/',AddCourse,name='addcourse'),
    path('addschool/',AddSchool,name='addschool'),
    path('addstudent/',AddStudent,name='addstudent'),
    path('coursereg/',CourseRegisters,name='coursereg'),
]