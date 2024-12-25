from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('Sign/', views.Sign, name='Sign'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('Comptes/', views.Comptes, name='Comptes'),
    path('Virements/', views.Virements, name='Virements'),
    path('mesinfo/', views.mesinfo, name='mesinfo'),
    path('virement_success/', views.virement_success, name='virement_success'),
    path('logout/', views.logout_view, name='logout')
]