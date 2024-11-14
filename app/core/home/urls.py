from django.urls import path
from core.home.views import home

app_name = "home"

urlpatterns = [
    #HOME
    path('',home.HomeView.as_view(),name="home"),
    path('noticias/', home.NewsView.as_view(), name='noticias'),
    #
]