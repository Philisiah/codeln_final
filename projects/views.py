from django.shortcuts import render

from projects.models import Project, ProjectType, DevType
# def project_category_list(request):
#     # list all project from above category
#     # filter projects by framework, language
#     pass
from transactions.forms import StackForm


# Create your views here.
# def project_categories(request):
#     # list all project categories
#     if request.method == 'GET':
#         return render(request, 'projects/categories.html', {})
#     elif request.method == 'POST':
#         return HttpResponse('<h2> Done </h2>')


def project_list(request, id):
    # TODO: filter projects by framework, language and category using django filter
    categoryname = ProjectType.objects.get(id=id)

    projecttypes = Project.objects.filter(projecttype_id=id)
    return render(request, 'projects/all_projects.html', {'projecttypes': projecttypes, 'categoryname': categoryname})


def dev_type_view(request, slug):
    dev_type = DevType.objects.get(slug=slug)
    projects = Project.objects.filter(devtype=dev_type)
    return render(request, 'projects/dev_type.html', {'projects': projects, 'dev_type': dev_type})


def project_type_view(request, slug):
    project_type = ProjectType.objects.get(slug=slug)
    projects = Project.objects.filter(projecttype=project_type)
    return render(request, 'projects/project_type.html', {'projects': projects, 'project_type': project_type})


def categories_view(request):
    project_types = ProjectType.objects.all()
    dev_types = DevType.objects.all()
    return render(request, 'projects/categories.html', {'project_types': project_types, 'dev_types': dev_types})


def project_view(request, id):
    project = Project.objects.get(id=id)
    stack_form = StackForm()
    return render(request, 'projects/project.html', {'project': project, 'stack_form': stack_form})
