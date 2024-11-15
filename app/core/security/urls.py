from django.urls import path
from core.security.views import auth, client

app_name = "security"

urlpatterns = [
    #Security
    path('login/', auth.LoginView.as_view(), name='login'),
    path('register/', auth.RegisterView.as_view(), name='register'),
    path('logout/', auth.user_logout, name='logout'),

    #CLIENT
    path('clients/', client.ClientListView.as_view(), name='client_list'),
]