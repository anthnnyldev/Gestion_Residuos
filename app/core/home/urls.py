from django.urls import path
from core.home.views import home, data
from .views.data import country_detail

app_name = "home"

urlpatterns = [
    #HOME
    path('',home.HomeView.as_view(),name="home"),
    path('noticias/', home.NewsView.as_view(), name='noticias'),
    path('tutorial/', home.TutorialView.as_view(), name='tutorial'),
    path('about/', home.AboutView.as_view(), name='about'),
    path('contacto/', home.ContactosView.as_view(), name='contacto'),
    path('datos/', data.load_waste_data, name='datos'),
    path('country/<str:country_name>/', country_detail, name='country_detail'),
    


]