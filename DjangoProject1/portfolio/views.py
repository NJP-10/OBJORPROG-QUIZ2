from django.shortcuts import render, get_object_or_404
from models import Portfolio, Project


# Create your views here.

def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/list.html', {'portfolios': portfolios})


def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project.html', {'projects': projects})