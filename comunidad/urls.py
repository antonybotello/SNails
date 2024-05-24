from django.contrib import admin
from django.urls import path
from comunidad import views as html_views
urlpatterns = [
    path('usuarios/', html_views.usuario_list_view, name='usuario_list_view'),
    path('usuarios/<int:pk>/', html_views.usuario_detail_view, name='usuario_detail_view'),
]
