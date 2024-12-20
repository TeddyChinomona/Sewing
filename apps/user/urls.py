from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', LogInView, name= 'login_view'),
    path('register/', RegisterView, name= 'register_view')
]
