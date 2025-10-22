from django.urls import path
from . import views

urlpatterns = [
    path('<str:entidade>/', views.listar_objetos, name='listar'),
    path('<str:entidade>/novo/', views.criar_objeto, name='criar'),
    path('<str:entidade>/<int:pk>/editar/', views.editar_objeto, name='editar'),
    path('<str:entidade>/<int:pk>/deletar/', views.deletar_objeto, name='deletar'),
    path('base/', views.base_view, name='base'),
    path('', views.dashboard, name='dashboard'),


]
