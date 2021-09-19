from django.urls import path
from .views import PatientListView, PatientDetailView
from . import views

urlpatterns = [
    path('', PatientListView.as_view(), name='database-home'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('about/', views.about, name='database-about'),
]