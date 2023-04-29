from django.urls import path
from .views import RegisterPage, LoginPage,ChangeProfile

urlpatterns =[
    path('', RegisterPage.as_view(), name='register'),
    path('login', LoginPage, name='login'),
    path('change-profile', ChangeProfile, name='change-profile'),

]

