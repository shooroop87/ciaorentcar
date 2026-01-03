from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # Главная
    path("", views.index, name="index"),
    
    # Информационные страницы
    path("kontakt/", views.contact, name="contact"),
    
    # Правовые страницы
    path("cookies/", TemplateView.as_view(template_name="pages/cookies.html"), name="cookies"),

]