from django.urls import path
from users.views import register, login, landing

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('landing/', landing, name='landing'),
]