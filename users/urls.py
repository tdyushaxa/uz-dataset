from django.urls import path
from .views import RegisterPage, LoginPage,ChangeProfile,Dashboard,Logout

urlpatterns =[
    path('', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage, name='login'),
    path('logout/', Logout, name='logout'),
    path('change-profile/', ChangeProfile, name='change-profile'),
    path('dashboard/',Dashboard,name='dashboard')

]

