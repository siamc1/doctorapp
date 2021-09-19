from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required

patients = [
    {
        'name': 'John Smith',
        'DOB': 'April 4, 2002',
        'sex': 'Male',
        'blood_pressure': 'High',
        'risk_factor': 0.3
    },
    {
        'name': 'Jane Doe',
        'DOB': 'September 20, 1994',
        'sex': 'Female',
        'blood_pressure': 'Moderate',
        'risk_factor': 0.1
    }
]

@login_required()
def home(request):
    context = {
        'patients': Patient.objects.all()
    }
    return render(request, 'database/patients.html', context)

@login_required()
def profile(request):
    return render(request, 'database/profile.html')

def about(request):
    return render(request, 'database/about.html')
