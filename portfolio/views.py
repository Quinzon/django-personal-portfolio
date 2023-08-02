from django.shortcuts import render
from .models import Project
from .models import Resume


def portfolio(request):
    projects = Project.objects.all()
    resume = Resume.objects.first()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'resume': resume})
