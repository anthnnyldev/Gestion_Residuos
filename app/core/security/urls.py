from django.urls import path
from core.security.views import auth

app_name = "security"

urlpatterns = [
    #Security
    path('login/', auth.LoginView.as_view(), name='login'),
    path('register/', auth.RegisterView.as_view(), name='register'),
]