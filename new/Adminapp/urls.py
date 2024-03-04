from django.urls import path
from . import views

app_name = 'madmin'

urlpatterns = [
    
    
    path('registeradmin/',views.registeradmin,name='registeradmin'),
    path('loginadmin/',views.loginadmin,name='loginadmin')

    
]