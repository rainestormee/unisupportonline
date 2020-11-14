from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='uso-home'),
    path('about/', views.about, name='uso-about'),
    path('contact/', views.contact, name='uso-about'),
    path('dashboard/', views.dashboard, name='uso-about'),
    path('help/', views.help, name='uso-about'),
    path('login/', views.login, name='uso-about'),
    path('search/', views.search, name='uso-about'),
    path('signup/', views.signup, name='uso-about'),
    path('terms/', views.terms, name='uso-about'),

]
