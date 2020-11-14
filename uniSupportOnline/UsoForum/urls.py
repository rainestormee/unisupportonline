from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name='uso-home'),
    path('forum/',views.forum, name='uso-forums'),
    path('about/',views.about, name='uso-about')
]