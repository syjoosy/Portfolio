from django.shortcuts import render
from .models import Skills
from django.views.generic import ListView,DetailView

def HomePage(request):
    return render(request, 'skills/home.html')

class SkillDetailPage(DetailView):
    model = Skills
    template_name = 'skills/skill-detail.html'

class Works(ListView):
    model = Skills
    template_name = 'skills/myworks.html'
    context_object_name = 'skills'
    ordering = ['-id']

def Me(request):
    return render(request, 'skills/me.html')