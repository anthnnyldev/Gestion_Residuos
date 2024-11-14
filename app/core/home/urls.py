from django.urls import path
from core.home.views import home

app_name = "home"

urlpatterns = [
    #HOME
    path('',home.HomeView.as_view(),name="home"),
    path('noticias/', home.NoticiasView.as_view(), name='noticias'),
    path('tutorial/', home.TutorialView.as_view(), name='tutorial'),
    path('sobre-nosotros/', home.SobreNosotrosView.as_view(), name='sobre_nosotros'),
    path('contacto/', home.ContactoView.as_view(), name='contacto'),
    path('login/', home.LoginView.as_view(), name='login'),
]