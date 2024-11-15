from django.urls import path
from core.home.views import home, data
from .views.data import country_detail

app_name = "home"

urlpatterns = [
    #HOME
    path('',home.HomeView.as_view(),name="home"),
    path('about/', home.AboutView.as_view(), name='about'),
    path('datos/', data.load_waste_data, name='datos'),
    path('country/<str:country_name>/', country_detail, name='country_detail'),
    


]