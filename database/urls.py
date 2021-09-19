from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='database-home'),
    path('profile/', views.profile, name='database-profile'),
    path('about/', views.about, name='database-about'),
]