from django.urls import path
from .views import  register,signin,profile,signout
urlpatterns = [
    path('',register,name='signup'),
    path('signin/',signin,name ='signin'),
    path('profile/',profile,name ="profile"),
    path('logout',signout,name ='logout'),
]