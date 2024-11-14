from django.urls import path
from core.security.views import security

app_name = "security"

urlpatterns = [
    #Security
    path('login/', security.LoginView.as_view(), name='login'),
    path('register/', security.RegisterView.as_view(), name='register'),
]