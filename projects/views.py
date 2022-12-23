from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project

# Create your views here.
# def project_list(request):
#     return render(request, template_name='projects/index.html')


def all_projects(request: WSGIRequest) -> HttpResponse:
    # query db and return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})


def project_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})
