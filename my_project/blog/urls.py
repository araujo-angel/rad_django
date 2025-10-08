from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("eco/<str:textoUrl>", views.eco),
    path("info/", views.info),
    path('nome/', views.nome, name='nome'),
    path('condicionais/', views.condicionais, name='condicionais'),
    path('loops/', views.loops, name='loops'),
    path('', views.home, name='home'),
    path('contato/<int:telefone>/', views.contato, name='contato'),
    path('about/', views.about, name='about'),
]