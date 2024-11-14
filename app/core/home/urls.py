from django.urls import path
from core.home.views import home,NoticiasView, TutorialView, SobreNosotrosView, ContactoView, LoginView

app_name = "home"

urlpatterns = [
    #HOME
    path('',home.HomeView.as_view(),name="home"),
    path('noticias/', NoticiasView.as_view(), name='noticias'),
    path('tutorial/', TutorialView.as_view(), name='tutorial'),
    path('sobre-nosotros/', SobreNosotrosView.as_view(), name='sobre_nosotros'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('login/', LoginView.as_view(), name='login'),