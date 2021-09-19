from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Patient
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    context = {
        'patients': Patient.objects.all()
    }
    return render(request, 'database/patients.html', context)

class PatientListView(ListView):
    model = Patient
    template_name = 'database/patients.html'
    context_object_name = 'patients'
    ordering = ['-risk_factor']

class PatientDetailView(DetailView):
    model = Patient

@login_required()
def profile(request):
    return render(request, 'database/patient_detail.html')

def about(request):
    return render(request, 'database/about.html')
