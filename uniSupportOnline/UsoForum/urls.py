from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='uso-home'),
    path('about/', views.about, name='uso-about'),
    path('contact/', views.contact, name='uso-contact'),
    path('dashboard/', views.dashboard, name='uso-dashboard'),
    path('help/', views.help, name='uso-help'),
    path('login/', views.login, name='uso-login'),
    path('search/', views.search, name='uso-search'),
    path('signup/', views.signup, name='uso-signup'),
    path('terms/', views.terms, name='uso-terms'),
    path('loginCode/', views.loginCode),
    path('signupCode/', views.signupCode),
    path('discussions/',views.discussions, name='uso-discussions')
    # path('helpCode/',views.helpCode)
]
